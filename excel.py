import openpyxl

def make_excel(file_name):
    wb = openpyxl.Workbook()
    ws = wb.worksheets[0]
    header = ['No.', '종류', '작성자', '조회수', '작성 날짜', '제목', '링크', '내용 / 댓글']
    ws.column_dimensions['A'].width = 5
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 25
    ws.column_dimensions['D'].width = 7
    ws.column_dimensions['E'].width = 25
    ws.column_dimensions['F'].width = 60
    ws.column_dimensions['G'].width = 60
    ws.column_dimensions['H'].width = 100
    ws.append(header)
    wb.save(file_name)

def append_excel(file_name, item, start_idx=1):
    wb = openpyxl.load_workbook(file_name)
    ws = wb.worksheets[0]

    idx = start_idx * 1
    for it in item:
        row = [idx, '게시글', it['author'], it['view'], it['date'], it['title'], it['link'], it['contents']]
        ws.append(row)
        idx += 1
        # 댓글 추가
        for comment in it['comments']:
            row2 = ['', '댓글', comment['author'], '', comment['date'], '', '', comment['comment']]
            ws.append(row2)
    
    wb.save(file_name)

    return idx + 1
