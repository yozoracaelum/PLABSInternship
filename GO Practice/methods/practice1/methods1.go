package main

import "fmt"

type Contact struct {
	name string
	age  int
}

func welcome(x Contact) {
	fmt.Println(x.name)
	fmt.Println(x.age)
}
func main() {
	x := Contact{"James", 42}
	welcome(x)
}
