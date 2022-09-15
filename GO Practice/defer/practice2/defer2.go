package main

import "fmt"

func main() {
	fmt.Println("start")

	for i := 0; i < 5; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("end")
}
