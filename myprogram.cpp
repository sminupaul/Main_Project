#include<iostream>
#include<qd.hpp>
int main() {
	int counter = 0;
	qdlock lock;
	std::thread threads[4];
	for(auto& t : threads) {
		t = std::thread(
			[&lock, &counter]() {
				lock.delegate_n([&counter]() { counter++; });
			}
		);
	}
	for(auto& t : threads) {
	  t.join();
	}
	std::cout << "The counter value is " << counter << std::endl;
}
