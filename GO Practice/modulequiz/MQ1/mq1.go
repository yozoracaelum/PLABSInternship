package main

import "fmt"

func f(v ...int) {
	res := 20
	for _, a := range v {
		res -= a
		fmt.Println(res)
	}
	fmt.Println(res)
}
func main() {
	v := []int{8, 5, 3}
	f(v...)
}
