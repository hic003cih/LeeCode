package leetcode

func Solution(A []int, X int, Y int, Z int) int {
	// 初始化三個加油機，分別存儲剩餘燃料量和可用時間
	dispensers := []struct {
		fuel    int // 剩餘燃料
		readyAt int // 加油機下一次可用的時間
	}{
		{X, 0}, {Y, 0}, {Z, 0}, // 對應加油機 X, Y, Z
	}

	maxWait := 0 // 記錄最大等待時間

	for _, demand := range A {
		bestDispenser := -1       // 當前選擇的加油機索引
		earliestReady := int(1e9) // 最早可用的時間，初始化為一個很大的值

		// 遍歷三個加油機，找到可以滿足需求的最佳加油機
		for i := 0; i < 3; i++ {
			if dispensers[i].fuel >= demand && dispensers[i].readyAt < earliestReady {
				bestDispenser = i
				earliestReady = dispensers[i].readyAt
			}
		}

		// 如果沒有加油機可以滿足需求，返回 -1
		if bestDispenser == -1 {
			return -1
		}

		// 計算當前車輛的等待時間
		waitTime := dispensers[bestDispenser].readyAt
		if waitTime > maxWait {
			maxWait = waitTime // 更新最大等待時間
		}

		// 更新加油機的剩餘燃料和下一次可用時間
		dispensers[bestDispenser].fuel -= demand
		dispensers[bestDispenser].readyAt += demand
	}

	return maxWait // 返回最大等待時間
}
