class MedianFinder {
private:
    std::priority_queue<int> max_heap;
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
public:
    MedianFinder() {}
    
    void addNum(int num) {
        if (min_heap.empty()) {
            return min_heap.push(num);
        }

        if (max_heap.empty()) {
            return max_heap.push(num);
        }

        if (min_heap.size() <= max_heap.size()) {
            min_heap.push(num);
        } else {
            max_heap.push(num);
        }

        while (min_heap.top() < max_heap.top()) {
            int old_min = min_heap.top();
            int old_max = max_heap.top();
            min_heap.pop();
            max_heap.pop();
            
            min_heap.push(old_max);
            max_heap.push(old_min);
        }
    }
    
    double findMedian() {
        if (min_heap.size() == max_heap.size()) {
            return (min_heap.top() + max_heap.top()) / 2.0;
        } else if (min_heap.size() > max_heap.size()) {
            return min_heap.top();
        } else {
            return max_heap.top();
        }
    }   
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */