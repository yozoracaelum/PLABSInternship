package main

import (
	"fmt"
	"time"
)

func out(from, to int) {
	for i := from; i <= to; i++ {
		time.Sleep(1 * time.Second)
		fmt.Println(i)
	}
}
func main() {
	go out(0, 5)
	go out(6, 10)
}
