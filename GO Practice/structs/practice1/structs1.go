package main

import "fmt"

type Contact struct {
	name string
	age  int
}

func main() {
	x := Contact{"James", 42}

	x.age = 8
	fmt.Println(x.age)
	fmt.Println(x.name)
}
