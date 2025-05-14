print("Seja bem vindo ao quizz de animes!")
answer_user = input("Quer começar? (S/N)")
answer_user_upper = answer_user.upper()
print(answer_user_upper)

if answer_user_upper != "S":
    quit()

score = 0 

print("Começando...")

print("Quem é o padrinho do Naruto? \n (A) Minato \n (B)Jiraya \n (C)Orochimaru \n (D)Iruka")
answer1 = input("Resposta: ")

answer1_upper = answer1.upper()

if answer1_upper == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Quem é a mãe do Naruto? \n (A)Kushina \n (B)Tsunade \n (C)Sakura \n (D)Mei")
answer2 = input("Resposta: ")

answer2_upper = answer2.upper()

if answer2_upper == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")
    
print("Qual é a ciência do anime Fullmetal Alchemist ? \n (A)Biologia \n (B)Computação \n (C)Alquimia \n (D)Matemática")
answer3 = input("Resposta: ")

answer3_upper = answer3.upper()

if answer3_upper == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("No anime Black Clover, qual o nome do demonio que está dentro do Asta ? \n (A)Marce \n (B)Jud \n (C)Liebe \n (D)Iuno")
answer4 = input("Resposta: ")

answer4_upper = answer4.upper()

if answer4_upper == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"O quizz acabou!......... Pontuação: {score}")