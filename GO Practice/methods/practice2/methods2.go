package main

import "fmt"

type Contact struct {
	name string
	age  int
}

func (ptr *Contact) increase(val int) {
	ptr.age += val
}
func main() {
	x := Contact{"James", 42}
	x.increase(8)
	fmt.Println(x.age)
}
