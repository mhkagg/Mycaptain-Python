from ast import main
from operator import truediv
import csv

def write_into_csv(info_list):
    with open('students_info.csv', 'a' , newline='') as csv_file:
        writer= csv.writer(csv_file)
        
        if csv_file.tell() == 0 :
            writer.writerow(['name', 'age', 'contact info', 'email-id'])
        
        writer.writerow(info_list)

if __name__ == '__main__':
    
    condition = True
    student_num = 1
    while(condition): 
        student_info= input("enter information of student {} in the following format( Name Age Contact_number Email_ID): ". format(student_num))
        
        student_info_log= student_info.split(' ')
        
        print("Check entered information:\n NAME:{} \n AGE:{} \n CONTACT DETAILS:{} \n EMAIL_ID: {} " .format(student_info_log[0], student_info_log[1], student_info_log[2], student_info_log[3]))
        
        check= input("is the entered information correct? (yes/no): ")
        if check=="yes":
            write_into_csv(student_info_log)
            
            more_info= input(" do you want to enter information about another student (yes/no):")
            if more_info == "yes" :
                condition = True
                student_num = student_num + 1
            elif more_info == "no" :
                condition = False
        
        elif check =="no":
            print("PLEASE RE-ENTER STUDENT INFORMATION!")
