//1. Two Sum
#include <iostream>
#include <vector>
using namespace std;
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;
        for (int i=0; i<nums.size(); i++) {
            if (indices.find(target-nums[i]) != indices.end()) {
                return {indices[target-nums[i]], i};
            } else {
                indices[nums[i]] = i;
            }
        }
    
    return vector<int>{0,1};    //Dummy
    }
};


int main() {
    vector<int> nums = {2,7,11,15};
    vector<int> nums2 = {3,2,4};
    vector<int> nums3 = {3,3};

    vector<int> s = Solution().twoSum(nums, 9);
    vector<int> s2 = Solution().twoSum(nums2, 6);
    vector<int> s3 = Solution().twoSum(nums3, 6);

    (count(s.begin(), s.end(), 0) && count(s.begin(), s.end(), 1)) ? cout << "PASSED" : cout << "FAIL";
    (count(s2.begin(), s2.end(), 1) && count(s2.begin(), s2.end(), 2)) ? cout << "PASSED" : cout << "FAIL";
    (count(s3.begin(), s3.end(), 1) && count(s3.begin(), s3.end(), 0)) ? cout << "PASSED" : cout << "FAIL";

}