package main

import (
	"fmt"
	"time"
)

func main() {
	toggle := true
	for toggle {
		fmt.Println("Hello!!")
		time.Sleep(1 * time.Second)
	}
}
