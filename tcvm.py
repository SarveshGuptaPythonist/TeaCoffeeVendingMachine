import model 
class tcvm:
      choice=0
      tea = 2000
      coffee = 2000
      sugar = 8000
      water = 15000
      milk = 10000
      sale = []
      def startApp(self):
            while True:
                  self.printOptions()
                  if tcvm.choice == 1:
                        self.MakeCoffee()
                  elif tcvm.choice == 2:
                        self.MakeTea()
                  elif tcvm.choice == 3:
                        self.MakeBlackCoffee()
                  elif tcvm.choice == 4:
                        self.MakeBlackTea()
                  elif tcvm.choice == 5:
                        self.RefillContainer()
                  elif tcvm.choice == 6:
                        self.CheckTotalSale()
                  elif tcvm.choice == 7:
                        self.ContainerStatus()
                  elif tcvm.choice == 8:
                        self.ResetContainer()
                  elif tcvm.choice == 9:
                        self.Exit()
                  

      if (self.tea<0 or self.milk<0 or self.water<0 or self.sugar<0 or self.coffee<0):
            print('refill not filled')
            break
                        
      def printOptions(self):
            print('')
            print('')
            print('1. Make Coffee')
            print('2. Make Tea')
            print('3. Make Black Coffee')
            print('4. Make Black Tea')
            print('5. Refill Container')
            print('6. Check total sale')
            print('7. container status')
            print('8. Reset Container')
            print('9. Exit TCVM')
            try:
                  tcvm.choice = int(input('enter your choice: '))
            except:
                  print("Wrong Input.Try Again!!!!!")
            

      def MakeTea(self):
            try:
                  quantity = int(input('how many : '))
            except:
                  print("try again!")
            tcvm.tea=tcvm.tea-model.TeaCup.tea
            tcvm.water=tcvm.water-model.TeaCup.water
            tcvm.milk=tcvm.milk-model.TeaCup.milk
            tcvm.sugar=tcvm.sugar-model.TeaCup.sugar
            print("your tea is ready")
            print("the remaining tea coffee sugar water milk",tcvm.tea,tcvm.coffee,tcvm.sugar,tcvm.water,tcvm.milk)
            for i in range(0,quantity):
                  self.sale.append('tea')
            
            
      def MakeCoffee(self):
            try:
                  quantity = int(input('how many : '))
            except:
                  print("try again!")
            tcvm.coffee=tcvm.coffee-model.CoffeeCup.coffee
            tcvm.water=tcvm.water-model.CoffeeCup.water
            tcvm.milk=tcvm.milk-model.CoffeeCup.milk
            tcvm.sugar=tcvm.sugar-model.CoffeeCup.sugar
            print("your coffee is ready")
            print("the remaining tea coffee sugar water milk",tcvm.tea,tcvm.coffee,tcvm.sugar,tcvm.water,tcvm.milk)
            for i in range(0,quantity):
                  self.sale.append('coffee')

            
      def MakeBlackTea(self):
            try:
                  quantity = int(input('how many : '))
            except:
                  print("try again!")
            tcvm.tea=tcvm.tea-model.BlackTea.tea
            tcvm.water=tcvm.water-model.BlackTea.water
            tcvm.sugar=tcvm.sugar-model.BlackTea.sugar
            print("your tea is ready")
            print("the remaining tea coffee sugar water milk",tcvm.tea,tcvm.coffee,tcvm.sugar,tcvm.water,tcvm.milk)
            for i in range(0,quantity):
                  self.sale.append('blacktea')

            
      def MakeBlackCoffee(self):
            try:
                  quantity = int(input('how many : '))
            except:
                  print("try again!")
            tcvm.coffee=tcvm.coffee-model.BlackCoffee.coffee
            tcvm.water=tcvm.water-model.BlackCoffee.water
            tcvm.sugar=tcvm.sugar-model.BlackCoffee.sugar
            print("your coffee is ready")
            print("the remaining tea coffee sugar water milk",tcvm.tea,tcvm.coffee,tcvm.sugar,tcvm.water,tcvm.milk)
            for i in range(0,quantity):
                  self.sale.append('blackcoffee')

      
      def RefillContainer(self):
            password=int(input('Give password to refill:'))

            if (password == model.RefillPassword.password):
                  tea = 2000
                  coffee = 2000
                  sugar = 8000
                  water = 15000
                  milk = 10000

            else:
                  print('Incorrect Password!')


      def CheckTotalSale(self):
            tc = model.TeaCup.rate
            btc = model.BlackTea.rate
            cc = model.CoffeeCup.rate
            bcc = model.BlackCoffee.rate
            tcount=self.sale.count('tea')
            btcount=self.sale.count('blacktea')
            ccount=self.sale.count('coffee')
            bccount=self.sale.count('blackcoffee')
            
            password=int(input('Give password to check sale:'))
            if (password == model.CheckSale.password):
                  print('the tea are: ',tcount)
                  print('the blacktea are: ',btcount)
                  print('the coffee are: ',ccount)
                  print('the blackcoffee are: ',bccount)
                  print('the total sale is',(tc*tcount+btc*btcount+cc*ccount+bcc*bccount,'rs'))
                  

            else:
                  print('Incorrect Password!')

      
      def ContainerStatus(self):
            password=int(input('Give password to container status:'))
            if (password == model.ConatainerStatus.password):
                  print('tea container has: ',self.tea,'grams left!')
                  print('coffee container has: ',self.coffee,'grams left!')
                  print('milk container has: ',float((self.milk)/1000),'litre left!')
                  print('sugar container has: ',self.sugar,'grams left!')
                  print('water container has: ',float((self.water)/1000),'litre left!')

            else:
                  print('Incorrect Password!')


      def ResetContainer(self):
            password=int(input('Give password to reset container :'))
            if (password == model.ResetConatiner.password):
                  tea = model.ResetConatiner.password.tea
                  coffee = model.ResetConatiner.password.coffee
                  sugar = model.ResetConatiner.password.sugar
                  water = model.ResetConatiner.password.water
                  milk = model.ResetConatiner.password.milk
            
            else:
                  print('Incorrect Password!')


      def Exit(self):
            break


      
            
      
               
      






















work = tcvm()
work.startApp()
      
