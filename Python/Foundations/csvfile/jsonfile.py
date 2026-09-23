import json

stds={
        1:{
                
        }
}

with open(r"C:\Users\91636\OneDrive\Desktop\Data-Analytics-Portfolio\Python\Foundations\csvfile\s_data.json","a") as j_file:
    # read
    # student=json.load(j_file)

    # print(student["attendance"])
    # print(student["marks"]["Python"])

    # write
        
        student=json.dumps(stds)
        print(student)
    # print(student["marks"]["Python"])