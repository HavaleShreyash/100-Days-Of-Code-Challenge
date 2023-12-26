#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double MedianOfArrays(vector<int>& array1, vector<int>& array2) {
        int m = array1.size();
        int n = array2.size();

        // Ensure array1 is always the smaller array
        if (m > n) {
            return MedianOfArrays(array2, array1);
        }

        int low = 0, high = m;
        while (low <= high) {
            int partitionX = (low + high) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;

            int maxLeftX = (partitionX == 0) ? INT_MIN : array1[partitionX - 1];
            int minRightX = (partitionX == m) ? INT_MAX : array1[partitionX];

            int maxLeftY = (partitionY == 0) ? INT_MIN : array2[partitionY - 1];
            int minRightY = (partitionY == n) ? INT_MAX : array2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // Median found
                if ((m + n) % 2 == 0) {
                    // Even number of elements, return average of medians
                    return (double)(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2;
                } else {
                    // Odd number of elements, return the larger median
                    return (double)max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                high = partitionX - 1;
            } else {
                low = partitionX + 1;
            }
        }

        return -1; // Should never reach here
    }
};

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int m,n;
        cin>>m;
        vector<int> array1(m);
        for (int i = 0; i < m; ++i){
            cin>>array1[i];
        }
        cin>>n;
        vector<int> array2(n);
        for (int i = 0; i < n; ++i){
            cin>>array2[i];
        }
        Solution ob;
        cout<<ob.MedianOfArrays(array1, array2)<<endl;
    }
    return 0; 
}