// leetcode 
    int searchInsert(vector<int>& nums, int target) {
        int n=nums.size();
        int res=n, l=0, r=n-1;
        while(l<=r){
            int mid=(l+r)/2;
            if(nums[mid]==target) return mid;
            if(nums[mid]<target)
                l=mid+1;
            else{
                r=mid-1;
                res=mid;
            }
        }
        return res;
    int mySqrt(int x) {
        long long res, l=0, r=x;
        while(l<=r){
            long long m=r+(l-r)/2;
            if(m*m==x) return m;
            if(m*m<x){
                l=m+1;
            }
            else{
                r=m-1;
                res=m-1;
            }
        }
        return res;
    }
    int firstBadVersion(int n) {
        int l=1, r=n, res;
        while(l<=r){
            int mid=r+(l-r)/2;
            if(isBadVersion(mid)){
                res=mid;
                r=mid-1;
            }
            else l=mid+1;
        }
        return res;
    }
    bool isPerfectSquare(int num) {
        int l=0, r=num;
        while(l<=r){
            long long mid=(l+r)/2;
            if(mid*mid==num) return true;
            if(mid*mid>num) r=mid-1;
            else l=mid+1;
        }
        return false;
    }
    int guessNumber(int n) {
        int l=1, r=n, res;
        while(l<=r){
            long long mid=r+(l-r)/2;
            if(guess(mid)==0) return mid;
            if(guess(mid)==-1) r=mid-1;
            else if(guess(mid)==1) l=mid+1;
        }
        return 0;
    }
    int arrangeCoins(int n) {
        int l=1, r=n;
        while(l<=r){
            long long mid=r+(l-r)/2;
            long long cnt=mid*(mid+1)/2;
            if(cnt==n) return mid;
            if(cnt>n) r=mid-1;   
            else l=mid+1;
        }
        return r;
    }
    char nextGreatestLetter(vector<char>& letters, char target) {
        int l=0, r=letters.size()-1, res;
        if(target>=letters[r]) return letters[0];
        while(l<=r){
            int mid=r+(l-r)/2;
            if(target==letters[mid]) res=mid+1;
            if(target<letters[mid]){
                r=mid-1;
                res=mid;
            }
            else{
                l=mid+1;    
            }
        }
        return letters[res];
    }