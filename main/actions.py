from db import DB

def validate(email, password):
    result = DB().execute(f"select * from users where email = '{email}' and password = HashBytes('{password}')").fetchall()

    if result:
        return True
    return False


def registerUser(user_details):
    query  = f"""Insert into users values('{user_details["name"]}', 
    '{user_details["email"]}',
    '{user_details["dob"]}',
    '{user_details["gender"]}',
    HashBytes('{user_details["password"]}'))"""


def assess_results(answers):
    response = {}
    iterpretation = {1 : "VERY POOR", 2: "POOR", 3: "NEITHER POOR NOR GOOD", 4: "GOOD", 5: "VERY GOOD"}

    for i in range(len(answers)):
        answer = answers[i]
        answer = answer.split("_")[-1]

        answers[i] = int(answer)

    response["Quality of Life"] = iterpretation[answers[0]]
    response["Health"] = iterpretation[answers[1]]
    response["Physical"] = iterpretation[(answers[2] + answers[3] + answers[9] + answers[14] + answers[15] + answers[16] + answers[17])// 7]
    response["Pschyological"] = iterpretation[(answers[4] + answers[5] + answers[6] + answers[10] + answers[18] + answers[25]) // 6]
    response["Social"] = iterpretation[(answers[20] + answers[21] + answers[19]) // 3]
    response["Environment"] =  iterpretation[(answers[7] + answers[9] + answers[11] + answers[12] + answers[13] + answers[22] + answers[23] + answers[24]) // 8]

    print(response)
    return response
