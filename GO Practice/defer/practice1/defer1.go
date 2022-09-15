package main

import "fmt"

func welcome() {
	fmt.Println("Welcome")
}

func main() {
	defer welcome()
	fmt.Println("Hey")
}
