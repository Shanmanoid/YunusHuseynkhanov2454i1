def bank_account():
    init_deposit = int(input("Please enter an initial deposit: "))


    while True:
      action = input("Deposit(write D) or Withdraw(write W): ")
      value = int(input("Please enter the value of your action: "))
      if action == "d" or action == "D":
        init_deposit += value
        print(f"Your balance is {init_deposit}")
      elif action == "w" or action == "W":
        init_deposit -= value
        if init_deposit < 0:
          print("You can't go lower 0")
          init_deposit += value
          print(f"Your balance is {init_deposit}")
          continue
        print(f"Your balance is {init_deposit}")

bank_account()