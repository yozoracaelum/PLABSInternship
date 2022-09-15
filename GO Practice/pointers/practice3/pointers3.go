package main

import "fmt"

func scale(pt *float32, x float32) {
	*pt = *pt * x
}

func main() {
	var num float32
	var factor float32

	fmt.Scanln(&num)
	fmt.Scanln(&factor)

	scale(&num, factor)
	fmt.Println(num)
}
