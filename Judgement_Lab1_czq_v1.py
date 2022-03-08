import os
import subprocess
import filecmp
from timeit import default_timer as timer

# PATH info, maybe change somehow, playing petty tricks is useless =.=
puzzles_path = './puzzles'
TA_answers_path = './TA_answers'
student_project_path = './sudoku_solve'
TA_project_path = './TA_sudoku_solve'
student_answers_path = './student_answers'
ori_file_amount = 0
case_info_dir = './case_info'
test_files_list = []
input_cmd = ""
output_cmd = ""

'''
    global puzzles_path
    global TA_answers_path
    global student_project_path
    global TA_project_path
    global student_answer_path
    global ori_file_amount
    global case_info_path
    global test_files_list
    global input_cmd
    global output_cmd
'''


def check_before_all():
    # This func is going to check dir ./puzzles ./TA_answers and file ./sudoku_solve
    # By the way, get ready for ./Student_answers
    # Here we go! >u<

    global puzzles_path
    global TA_answers_path
    global student_project_path
    global TA_project_path
    global student_answers_path
    global ori_file_amount
    global test_files_list

    is_ready = True

    if not os.path.isfile(TA_project_path):
        is_ready = False
        print('Do not delete ./TA_sudoku_solve')
    if not os.path.isfile(student_project_path):
        print('NOTES: %s is not here, following try to make.' % student_project_path)
        f = subprocess.Popen('make', shell=True)
        f_code = f.wait()
        if not os.path.isfile(student_project_path):
            print('ERROR: Cannot make file %s'+ '\n' + 'Please chech your program or Makefile' % student_project_path)
            is_ready = False
    
    if not os.path.isdir(puzzles_path):
        print("ERROR: puzzles dir %s is not here, please ensure its exist." % puzzles_path)
        is_ready = False
    else:
        test_files_list = os.listdir(puzzles_path)
        for test_file in test_files_list:
            ori_file_amount = ori_file_amount + 1
    
    if is_ready:
        print('Totally load %d sudoku files.' % ori_file_amount)
        if not os.path.isdir(case_info_dir):
            os.mkdir(case_info_dir)
        if not os.path.exists(student_answers_path):
            os.mkdir(student_answers_path)
        if not os.path.exists(TA_answers_path):
            os.mkdir(TA_answers_path)
        del_list = os.listdir(student_answers_path)
        for del_file in del_list:
            del_file_path = os.path.join(student_answers_path, del_file)
            if os.path.isfile(del_file_path):
                os.remove(del_file_path)
    return is_ready


# def test_func():
#     s = 0
#     for i in range(1000):
#         for j in range(1000):
#             s = i + j


def running_TA():
    global TA_project_path
    global input_cmd
    global output_cmd
    f = subprocess.Popen(TA_project_path + input_cmd + output_cmd, shell=True)
    f_code = f.wait()


def running_student():
    global student_project_path
    global input_cmd
    global output_cmd
    f = subprocess.Popen(student_project_path + input_cmd + output_cmd, shell=True)
    f_code = f.wait()


def get_running_time(some_func):
    start_time = timer()
    some_func()
    owari_time = timer()
    return (owari_time - start_time)*1000


def test_basic():
    global TA_project_path
    global input_cmd
    global output_cmd
    global test_files_list
    global ori_file_amount
    print('Lab1 Basic test:')
    case_amount = ori_file_amount
    access_amount  = 0
    case_number = 0
    reference_score = 0.0
    for test_file in test_files_list:
        case_number = case_number + 1
        case_name = 'basic_case_' + str(case_number)
        case_info_path = os.path.join(case_info_dir,  case_name + '.txt')
        case_info = open(case_info_path, "w")
        case_info.write(os.path.join(puzzles_path, test_file)+'\n')
        case_info.close() 
        input_cmd = ' <' + case_info_path
        output_cmd = ' >' + os.path.join(student_answers_path, case_name + '.out')
        student_time = get_running_time(running_student)
        output_cmd = ' >' + os.path.join(TA_answers_path, case_name + '.out')
        TA_time = get_running_time(running_TA)
        
        print(case_name + ':', end=' ')
        is_access = filecmp.cmp(os.path.join(student_answers_path, case_name + '.out'), os.path.join(TA_answers_path, case_name + '.out'))
        if is_access:
            state_msg = 'accept!'
        else:
            state_msg = 'reject!'
        print('state is %s' % state_msg, end=' ')
        # print('TA used %d ms.' % TA_time, end=' ')
        if is_access:
            print('student used %d ms.' % student_time, end=' ')
            print('Performance score: ',end='')
            print('{:.2f}'.format(TA_time/student_time))
            access_amount = access_amount + 1
            reference_score = reference_score + TA_time/student_time
    print("Accept %d/%d cases. Reference performance score is %f." % (access_amount, case_amount, reference_score/case_amount))
        
    pass


def test_advanced():
    global TA_project_path
    global input_cmd
    global output_cmd
    global test_files_list
    global ori_file_amount
    print('Lab1 Advanced test:')
    case_amount = ori_file_amount
    access_amount  = 0
    case_number = 0
    reference_score = 0.0
    case_info_str = ''
    for test_file in test_files_list:
        case_number = case_number + 1
        case_name = 'advanced_case_' + str(case_number)
        case_info_path = os.path.join(case_info_dir,  case_name + '.txt')
        case_info = open(case_info_path, "w")
        case_info_str = case_info_str + os.path.join(puzzles_path, test_file)+'\n'
        case_info.write(case_info_str)
        case_info.close() 
        input_cmd = ' <' + case_info_path
        output_cmd = ' >' + os.path.join(student_answers_path, case_name + '.out')
        student_time = get_running_time(running_student)
        output_cmd = ' >' + os.path.join(TA_answers_path, case_name + '.out')
        TA_time = get_running_time(running_TA)
        
        print(case_name + ':', end=' ')
        is_access = filecmp.cmp(os.path.join(student_answers_path, case_name + '.out'), os.path.join(TA_answers_path, case_name + '.out'))
        if is_access:
            state_msg = 'accept!'
        else:
            state_msg = 'reject!'
        print('state is %s' % state_msg, end=' ')
        # print('TA used %d ms.' % TA_time, end=' ')
        if is_access:
            print('student used %d ms.' % student_time, end=' ')
            print('Performance score: ',end='')
            print('{:.2f}'.format(TA_time/student_time))
            access_amount = access_amount + 1
            reference_score = reference_score + TA_time/student_time
    print("Accept %d/%d cases. Reference performance score is %f." % (access_amount, case_amount, reference_score/case_amount))
    pass


def main():
    if check_before_all():
        test_basic()
        test_advanced()
        pass
    else:
        return


if __name__ == '__main__':
    main()
    pass