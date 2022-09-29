package main

import (
	"fmt"
	"time"
)

func main() {
	var now = time.Now()
	fmt.Println("year: ", now.Year(), "month: ", now.Month())
}
