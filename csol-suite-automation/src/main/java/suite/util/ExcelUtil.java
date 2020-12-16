package suite.util;

import java.io.File;
import java.io.FileInputStream;

import org.apache.poi.xssf.usermodel.XSSFWorkbook;

/**
 * Excel Utilities for the automation suite
 * 
 * @author arth.kumar
 *
 */
public class ExcelUtil {

	private XSSFWorkbook workbook;

	/**
	 * Input the excel path
	 * 
	 * @param excelPath path of the excel file
	 */
	public void ExcelDataConfig(String excelPath) {
		try {
			File filePath = new File(excelPath);
			FileInputStream Inputfile = new FileInputStream(filePath);
			workbook = new XSSFWorkbook(Inputfile);

		} catch (Exception e) {

			e.printStackTrace();
		}
	}

	/**
	 * Get data from cell of given sheet, row and column Number
	 * 
	 * @param sheetNumber  Index of the worksheet
	 * @param rowNumber    Row Number of the given worksheet
	 * @param columnNumber Row Number of the given worksheet
	 * @return value present inside the excel cell of given sheet based on the given
	 *         row and column Number
	 */
	public String getCellValue(int sheetNumber, int rowNumber, int columnNumber) {

		return workbook.getSheetAt(sheetNumber).getRow(rowNumber).getCell(columnNumber).getStringCellValue();
	}

	/**
	 * Get number of rows of the given worksheet
	 * 
	 * @param sheetIndex Index of the work sheet
	 * @return number of rows of the given sheet
	 */
	public int getRowCountFor(int sheetIndex) {

		return workbook.getSheetAt(sheetIndex).getLastRowNum() + 1;
	}
}