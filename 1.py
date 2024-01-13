import datetime  
import pickle  
  
def get_input(prompt):  
    while True:  
        try:  
            return int(input(prompt))  
        except ValueError:  
            print("请输入有效的整数！")  
  
def save_date():  
    year = get_input("请输入年份: ")  
    month = get_input("请输入月份: ")  
    day = get_input("请输入日期: ")  
    return datetime.datetime(year, month, day)  
  
def load_date():  
    try:  
        with open('input_date.pkl', 'rb') as f:  
            return pickle.load(f)  
    except FileNotFoundError:  
        return None  
    except Exception as e:  # 添加更广泛的异常处理  
        print(f"加载日期时出错: {e}")  
        return None  
  
def get_week_number(date):  
    week_number = date.isocalendar()[1]  
    return week_number  
  
def main():  
    global first_input_date  # 全局变量来保存输入的日期  
    first_input_date = load_date()  # 从文件中加载日期  
    if first_input_date is None:  # 如果未保存过日期，则获取并保存它  
        first_input_date = save_date()  
        with open('input_date.pkl', 'wb') as f:  # 将日期保存到文件  
            pickle.dump(first_input_date, f)  
        print("日期已保存！")  
    else:  # 如果已保存过日期，则加载它  
        print("已加载日期！")  
    current_date = datetime.datetime.now()  # 获取当前时间  
    current_year = current_date.year  # 获取当前年份  
    mark_year = first_input_date.year  # 获取标记的年份  
    if current_year == mark_year:  # 如果当前年份与标记的年份相同，计算周数差  
        current_week_number = current_date.isocalendar()[1]  # 获取当前周数  
        mark_week_number = get_week_number(first_input_date)  # 获取标记的周数  
        week_diff = current_week_number - mark_week_number  # 计算周数差并输出结果  
        if week_diff == 0:  # 如果当前时间与输入时间在同一周，输出数字“1”  
            print("1")  
        elif week_diff == 1:  # 如果是在标记时间所在周的第二周，输出数字“2”  
            print("2")  
        elif week_diff == 2:  # 如果是在标记时间所在周的第三周，输出数字“3”  
            print("3")  
        else:  # 否则，输出周数差  
            print(week_diff)  
    else:  # 如果当前年份与标记的年份不同，输出年份差并提示重新输入标记的日期和年份  
        year_diff = current_year - mark_year  # 计算年份差并输出结果  
        print(f"年份差为 {year_diff} 年。请重新输入标记的日期和年份。")  
            
if __name__ == "__main__":  # 主程序入口点  
    main()
