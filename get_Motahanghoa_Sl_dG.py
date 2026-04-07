import xlrd
import glob
import pandas as pd

def find_all_text_locations(file_path, search_texts, start_row=100, end_row=10000):
    """
    Find ALL occurrences of multiple texts in rows 100-10000
    Returns dictionary with text as key and list of row numbers as value
    """
    results = {text: [] for text in search_texts}
    
    try:
        wb = xlrd.open_workbook(file_path, formatting_info=False)
        sheet = wb.sheet_by_index(0)
        
        # Start from row 100 (index 99) to end_row or end of sheet
        start_idx = start_row - 1
        end_idx = min(end_row, sheet.nrows)
        
        for row_idx in range(start_idx, end_idx):
            for col_idx in range(sheet.ncols):
                cell_value = str(sheet.cell_value(row_idx, col_idx))
                
                # Check each search text
                for text in search_texts:
                    if text in cell_value:
                        if row_idx + 1 not in results[text]:  # Avoid duplicates in same row
                            results[text].append(row_idx + 1)
                        break  # Found one text in this row, move to next row
                        
        return results
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return results

def find_all_texts_with_details(file_path, search_texts, start_row=100, end_row=10000):
    """
    Find ALL occurrences with detailed information (row, column, value preview)
    """
    results = {text: [] for text in search_texts}
    
    try:
        wb = xlrd.open_workbook(file_path, formatting_info=False)
        sheet = wb.sheet_by_index(0)
        
        start_idx = start_row - 1
        end_idx = min(end_row, sheet.nrows)
        
        for row_idx in range(start_idx, end_idx):
            for col_idx in range(sheet.ncols):
                cell_value = str(sheet.cell_value(row_idx, col_idx))
                
                for text in search_texts:
                    if text in cell_value:
                        # Convert column index to letter
                        col_letter = get_column_letter(col_idx)
                        
                        results[text].append({
                            'row': row_idx + 1,
                            'column': col_letter,
                            'column_index': col_idx,
                            'value_preview': cell_value[:100]  # First 100 chars
                        })
                        break  # Found one text in this row
                        
        return results
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return results

def get_column_letter(col_idx):
    """
    Convert column index (0-based) to Excel column letter
    """
    result = ""
    while col_idx >= 0:
        result = chr(col_idx % 26 + 65) + result
        col_idx = col_idx // 26 - 1
    return result

def save_all_results_to_excel(all_files_results, output_file="all_locations.xlsx"):
    """
    Save all results to a single Excel file with multiple sheets
    """
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        
        # Sheet 1: Summary
        summary_data = []
        for file, results in all_files_results.items():
            for text, locations in results.items():
                if locations:
                    for loc in locations:
                        if isinstance(loc, dict):
                            summary_data.append({
                                'File': file,
                                'Search_Text': text,
                                'Row': loc['row'],
                                'Column': loc['column'],
                                'Value_Preview': loc['value_preview']
                            })
                        else:
                            summary_data.append({
                                'File': file,
                                'Search_Text': text,
                                'Row': loc,
                                'Column': '',
                                'Value_Preview': ''
                            })
        
        if summary_data:
            df_summary = pd.DataFrame(summary_data)
            df_summary.to_excel(writer, sheet_name='Summary', index=False)
        
        # Sheet 2, 3, 4: Separate sheets for each text type
        for text in ["Mô tả hàng hóa", "Số lượng (1)", "Đơn giá hóa đơn"]:
            sheet_data = []
            for file, results in all_files_results.items():
                locations = results.get(text, [])
                if locations:
                    for loc in locations:
                        if isinstance(loc, dict):
                            sheet_data.append({
                                'File': file,
                                'Row': loc['row'],
                                'Column': loc['column'],
                                'Value_Preview': loc['value_preview']
                            })
                        else:
                            sheet_data.append({
                                'File': file,
                                'Row': loc,
                                'Column': '',
                                'Value_Preview': ''
                            })
            
            if sheet_data:
                df = pd.DataFrame(sheet_data)
                # Create safe sheet name (remove special characters)
                sheet_name = text.replace(" ", "_").replace("(", "").replace(")", "")
                df.to_excel(writer, sheet_name=sheet_name[:31], index=False)  # Excel sheet name max 31 chars
        
        # Sheet 5: Statistics
        stats_data = []
        for file, results in all_files_results.items():
            for text, locations in results.items():
                stats_data.append({
                    'File': file,
                    'Search_Text': text,
                    'Count': len(locations),
                    'Rows': ', '.join([str(loc['row']) if isinstance(loc, dict) else str(loc) for loc in locations])
                })
        
        if stats_data:
            df_stats = pd.DataFrame(stats_data)
            df_stats.to_excel(writer, sheet_name='Statistics', index=False)
    
    print(f"\n✅ Results saved to: {output_file}")

# Main execution
def process_all_files():
    """
    Process all Excel files and find all three text locations
    """
    # Define search texts
    search_texts = ["Mô tả hàng hóa", "Số lượng (1)", "Đơn giá hóa đơn"]
    
    # Get all Excel files
    excel_files = glob.glob("*.xls") + glob.glob("*.xlsx")
    excel_files = [f for f in excel_files if not f.startswith("result_") and not f.startswith("all_locations")]
    
    if not excel_files:
        print("No Excel files found!")
        return
    
    print("="*80)
    print(f"SEARCHING FOR: {', '.join(search_texts)}")
    print(f"IN ROWS 100 TO 10000")
    print("="*80)
    
    all_results = {}
    
    for file in excel_files:
        print(f"\n📁 Processing: {file}")
        
        # Find all locations with details
        results = find_all_texts_with_details(file, search_texts, start_row=100, end_row=10000)
        
        all_results[file] = results
        
        # Display results
        for text in search_texts:
            locations = results[text]
            if locations:
                print(f"   ✅ '{text}': Found at {len(locations)} location(s)")
                for loc in locations[:3]:  # Show first 3
                    print(f"      → Row {loc['row']}, Column {loc['column']}")
                if len(locations) > 3:
                    print(f"      ... and {len(locations) - 3} more")
            else:
                print(f"   ❌ '{text}': Not found")
    
    # Save all results to Excel
    save_all_results_to_excel(all_results, "all_locations.xlsx")
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    for file, results in all_results.items():
        print(f"\n{file}:")
        for text in search_texts:
            count = len(results[text])
            print(f"   {text}: {count} occurrence(s)")

# Simple version - just row numbers (no details)
def simple_version():
    """
    Simple version - just return row numbers for each text
    """
    search_texts = ["Mô tả hàng hóa", "Số lượng (1)", "Đơn giá hóa đơn"]
    excel_files = glob.glob("*.xls") + glob.glob("*.xlsx")
    
    all_data = []
    
    for file in excel_files:
        results = find_all_text_locations(file, search_texts, start_row=100, end_row=10000)
        
        for text, rows in results.items():
            if rows:
                for row in rows:
                    all_data.append({
                        'File': file,
                        'Search_Text': text,
                        'Row': row
                    })
            else:
                all_data.append({
                    'File': file,
                    'Search_Text': text,
                    'Row': 'Not found'
                })
    
    # Save to Excel
    df = pd.DataFrame(all_data)
    output_file = "simple_locations.xlsx"
    df.to_excel(output_file, index=False)
    print(f"\n✅ Simple results saved to: {output_file}")

if __name__ == "__main__":
    # Run the main function with detailed results
    process_all_files()
    
    # Uncomment below for simple version (row numbers only)
    # simple_version()