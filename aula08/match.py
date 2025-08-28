num = input()
match num:
    case "1" | "2" | "3" | "4" | "5":
        print(f"você digitou: {num}")
    case _:
        print("O valor digitado não existe")
