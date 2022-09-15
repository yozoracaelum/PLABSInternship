package main

import "fmt"

type BankAccount struct {
	holder  string
	balance int
}

func (pt *BankAccount) withdraw(am int) {
	if pt.balance < am {
		fmt.Println("Insufficient Funds")
	} else {
		pt.balance = pt.balance - am
	}
}

func main() {
	acc := BankAccount{"James Smith", 10000}

	var amount int
	fmt.Scanln(&amount)

	acc.withdraw(amount)
	fmt.Println(acc)
}
