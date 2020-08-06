import os
from collections import defaultdict
import matplotlib.pylab as plt

document_reason = ['visual_authenticity', 'image_integrity', 'face_detection', 'image_quality', 'supported_document',
                   'conclusive_document', 'colour_picture',
                   'data_validation', 'data_consistency', 'data_comparison', 'police_record', 'compromised_document']
document_reason_dic = {'visual_authenticity': 0, 'image_integrity': 0, 'face_detection': 0, 'image_quality': 0,
                       'supported_document': 0, 'conclusive_document': 0, 'colour_picture': 0,
                       'data_validation': 0, 'data_consistency': 0, 'data_comparison': 0, 'police_record': 0,
                       'compromised_document': 0}

facial_reason = ['face_comparison_result',
                 'facial_image_integrity_result', 'visual_authenticity_result']
document_facial_dic = {'face_comparison_result': 0,
                       'facial_image_integrity_result': 0, 'visual_authenticity_result': 0}


def find_document_reason(checklist):
    reason_list = []
    for item in range(len(checklist)):
        if checklist[item] == "consider":
            reason_list.append(document_reason[item])
            document_reason_dic[document_reason[item]] += 1
    return reason_list


def find_facial_reason(checklist):
    reason_list = []
    for item in range(len(checklist)):
        if checklist[item] == "consider":
            reason_list.append(facial_reason[item])
            document_facial_dic[facial_reason[item]] += 1
    return reason_list


user_dic = defaultdict(list)
attempt_dic = defaultdict(list)


def check():
    pass_document_dic = defaultdict(list)
    fail_document_dic = defaultdict(list)

    pass_facial_dic = defaultdict(list)
    fail_facial_dic = defaultdict(list)

    document = os.getcwd() + '/doc_reports.csv'
    non_clear_image = 0
    clear_image = 0
    non_2_image_integrity_result = 0
    non_image_integrity_result = 0
    non_2_face_detection_result = 0
    non_face_detection_result = 0
    non_2_image_quality_result = 0
    non_image_quality_result = 0
    non_2_supported_document_result = 0
    non_supported_document_result = 0
    non_2_conclusive_document_quality_result = 0
    non_conclusive_document_quality_result = 0
    non_2_colour_picture_result = 0
    non_colour_picture_result = 0
    non_2_data_validation_result = 0
    non_data_validation_result = 0
    non_2_data_consistency_result = 0
    non_data_consistency_result = 0
    non_2_data_comparison_result = 0
    non_data_comparison_result = 0
    non_2_police_record_result = 0
    non_police_record_result = 0
    non_2_compromised_document_result = 0
    non_compromised_document_result = 0
    non_2_sub_result = 0
    non_sub_result = 0
    non_clear_attempt = 0
    non_1_image_integrity_result = 0

    non_1_face_detection_result = 0

    non_1_image_quality_result = 0

    non_1_supported_document_result = 0

    non_1_conclusive_document_quality_result = 0

    non_1_colour_picture_result = 0

    non_1_data_validation_result = 0

    non_1_data_consistency_result = 0

    non_1_data_comparison_result = 0

    non_1_police_record_result = 0

    non_1_compromised_document_result = 0

    non_1_sub_result = 0
    with open(document) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        pass_customer = 0
        fail_customer = 0
        for row in csv_reader:
            if row[2] == "clear":
                pass_customer += 1
                if (len(user_dic[row[1]]) > 0 and user_dic[row[1]][0] != 'Pass'):
                    user_dic[row[1]][0] = 'Pass'
                else:
                    user_dic[row[1]].append('Pass')
                if (len(attempt_dic[row[14]]) > 0):
                    attempt_dic[row[14]][0] = 'Pass'
                else:
                    attempt_dic[row[14]].append('Pass')
            else:
                if (len(user_dic[row[1]]) > 0 and user_dic[row[1]][0] != 'Pass'):
                    user_dic[row[1]][0] = 'Fail'
                else:
                    user_dic[row[1]].append('Fail')
                if (len(attempt_dic[row[14]]) > 0):
                    attempt_dic[row[14]][0] = 'Fail'
                else:
                    attempt_dic[row[14]].append('Fail')
                reason = row[3:7] + row[8:14] + row[16:18]
                reason_list = find_document_reason(reason)
                fail_customer = fail_customer + 1
                if (row[4] == "consider"):
                    non_2_image_integrity_result = non_2_image_integrity_result + 1
                if (row[5] == "consider"):
                    non_2_face_detection_result = non_2_face_detection_result + 1
                if (row[6] == "unidentified"):
                    non_2_image_quality_result = non_2_image_quality_result + 1
                if (row[8] == "unidentified"):
                    non_2_supported_document_result = non_2_supported_document_result + 1
                if (row[9] == "consider"):
                    non_2_conclusive_document_quality_result = non_2_conclusive_document_quality_result + 1
                if (row[10] == "consider"):
                    non_2_colour_picture_result = non_2_colour_picture_result + 1
                if (row[11] == "consider"):
                    non_2_data_validation_result = non_2_data_validation_result + 1
                if (row[12] == "consider"):
                    non_2_data_consistency_result = non_2_data_consistency_result + 1
                if (row[13] == "consider"):
                    non_2_data_comparison_result = non_2_data_comparison_result + 1
                if (row[15] == "consider"):
                    non_2_police_record_result = non_2_police_record_result + 1
                if (row[16] == "consider"):
                    non_2_compromised_document_result = non_2_compromised_document_result + 1
                if (row[18] == "consider"):
                    non_2_sub_result = non_2_sub_result + 1
                non_clear_attempt = non_clear_attempt + 1
            count += 1
            if (row[4] == "consider"):
                non_image_integrity_result = non_image_integrity_result + 1
            if (row[5] == "consider"):
                non_face_detection_result = non_face_detection_result + 1
            if (row[6] == "unidentified"):
                non_image_quality_result = non_image_quality_result + 1
            if (row[8] == "unidentified"):
                non_supported_document_result = non_supported_document_result + 1
            if (row[9] == "consider"):
                non_conclusive_document_quality_result = non_conclusive_document_quality_result + 1
            if (row[10] == "consider"):
                non_colour_picture_result = non_colour_picture_result + 1
            if (row[11] == "consider"):
                non_data_validation_result = non_data_validation_result + 1
            if (row[12] == "consider"):
                non_data_consistency_result = non_data_consistency_result + 1
            if (row[13] == "consider"):
                non_data_comparison_result = non_data_comparison_result + 1
            if (row[15] == "consider"):
                non_police_record_result = non_police_record_result + 1
            if (row[16] == "consider"):
                non_compromised_document_result = non_compromised_document_result + 1
            if (row[16] == "consider"):
                non_sub_result = non_sub_result + 1
            if (bool(row[4])):
                non_1_image_integrity_result = non_1_image_integrity_result + 1
            if (bool(row[5])):
                non_1_face_detection_result = non_1_face_detection_result + 1
            if (bool(row[6])):
                non_1_image_quality_result = non_1_image_quality_result + 1
            if (bool(row[8])):
                non_1_supported_document_result = non_1_supported_document_result + 1
            if (bool(row[9])):
                non_1_conclusive_document_quality_result = non_1_conclusive_document_quality_result + 1
            if (bool(row[10])):
                non_1_colour_picture_result = non_1_colour_picture_result + 1
            if (bool(row[11])):
                non_1_data_validation_result = non_1_data_validation_result + 1
            if (bool(row[12])):
                non_1_data_consistency_result = non_1_data_consistency_result + 1
            if (bool(row[13])):
                non_1_data_comparison_result = non_1_data_comparison_result + 1
            if (bool(row[15])):
                non_1_police_record_result = non_1_police_record_result + 1
            if (bool(row[16])):
                non_1_compromised_document_result = non_1_compromised_document_result + 1
            if (bool(row[16])):
                non_1_sub_result = non_1_sub_result + 1
    print("probability of image_integrity_result",
          non_2_image_integrity_result / non_clear_attempt)
    print("probability of face_detection_result",
          non_2_face_detection_result / non_clear_attempt)
    print("probability of image_quality_result",
          non_2_image_quality_result / non_clear_attempt)
    print("probability of supported_document_result",
          non_2_supported_document_result / non_clear_attempt)
    print("probability of conclusive_document_quality_result",
          non_2_conclusive_document_quality_result / non_clear_attempt)
    print("probability of non_2_colour_picture_result",
          non_2_colour_picture_result / non_clear_attempt)
    print("probability of data_validation_result",
          non_2_data_validation_result / non_clear_attempt)
    print("probability of data_consistency_result",
          non_2_data_consistency_result / non_clear_attempt)
    print("probability of data_comparison_result",
          non_2_data_comparison_result / non_clear_attempt)
    print("probability of police_record_result",
          non_2_police_record_result / non_clear_attempt)
    print("probability of compromised_document_result",
          non_2_compromised_document_result / non_clear_attempt)
    print("probability of sub_result", non_2_sub_result / non_clear_attempt)
    facial = os.getcwd() + '/facial_similarity_reports.csv'
    with open(facial) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0

        for row in csv_reader:
            if row[2] == "clear":
                pass_customer += 1
                if (len(user_dic[row[1]]) > 1 and user_dic[row[1]][0] != 'Pass'):
                    user_dic[row[1]][0] = 'Pass'
                else:
                    user_dic[row[1]].append('Pass')
                if (len(attempt_dic[row[8]]) > 1):
                    attempt_dic[row[8]][1] = 'Pass'
                else:
                    attempt_dic[row[8]].append('Pass')
            else:
                if (len(user_dic[row[1]]) > 1 and user_dic[row[1]][0] != 'Pass'):
                    user_dic[row[1]][1] = 'Fail'
                else:
                    user_dic[row[1]].append('Fail')
                if (len(attempt_dic[row[8]]) > 1):
                    attempt_dic[row[8]][1] = 'Fail'
                else:
                    attempt_dic[row[8]].append('Fail')
                reason = row[3:4] + row[5:7]
                reason_list = find_facial_reason(reason)
                fail_customer = fail_customer + 1
            count += 1
    sort_document_reason_dic = sorted(
        document_reason_dic.items(), key=lambda x: x[1], reverse=True)
    lists = sorted(document_reason_dic.items())
    x, y = zip(*lists)
    plt.plot(x, y)
    plt.show()
    sorted_facial_reason_dic = sorted(
        document_facial_dic.items(), key=lambda x: x[1], reverse=True)
    lists = sorted(document_facial_dic.items())
    x, y = zip(*lists)
    plt.figure(figsize=(20, 10))
    plt.plot(x, y)
    plt.show()
    print(sorted_facial_reason_dic)
    total_pass = 0
    total_user = 0
    total_fail = 0
    first_test_fail = 0
    second_test_fail = 0

    for key, value in user_dic.items():
        result = value
        if result[0] == 'Fail':
            first_test_fail += 1
        if result[1] == 'Fail':
            second_test_fail += 1
        if result[0] == "Pass" and result[1] == "Pass":
            total_pass += 1
        else:
            total_fail += 1
        total_user += 1
    total_pass_attempt = 0
    total_user_attempt = 0
    total_fail_attempt = 0
    first_test_fail_attempt = 0
    second_test_fail_attempt = 0
    for key, value in attempt_dic.items():
        result = value
        if (len(result) == 2):
            if result[0] == 'Fail':
                first_test_fail_attempt += 1
            if result[1] == 'Fail':
                second_test_fail_attempt += 1
            if result[0] == "Pass" and result[1] == "Pass":
                total_pass_attempt += 1
            else:
                total_fail_attempt += 1
            total_user_attempt += 1
    print('Total User = ', total_user)
    print('Total Fail = ', total_fail)
    print('Total Pass = ', total_pass)
    print('Document fail = ', first_test_fail)
    print('Facial Similarity Fail = ', second_test_fail)
    pass_rate = total_pass / (total_user)
    print('Pass rate = ', pass_rate)
    print('Total User = ', total_user_attempt)
    print('Total Fail = ', total_fail_attempt)
    print('Total Pass = ', total_pass_attempt)
    print('Document fail = ', first_test_fail_attempt)
    print('Facial Similarity Fail = ', second_test_fail_attempt)
    pass_rate_attempt = total_pass_attempt / (total_user_attempt)
    print('Pass rate = ', pass_rate_attempt)


check()
