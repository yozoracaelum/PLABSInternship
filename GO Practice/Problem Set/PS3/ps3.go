package main

import "fmt"

func main() {
	results := []string{"w", "l", "w", "d", "w", "l", "l", "l", "d", "d", "w", "l", "w", "d"}
	score := 0
	var sc string
	fmt.Scanln(&sc)
	results = append(results, sc)
	for _, v := range results {
		if v == "w" {
			score += 3
		}
		if v == "d" {
			score += 1
		}
	}
	fmt.Println(score)
}
