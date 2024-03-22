#include<stdio.h>
#include <stdlib.h>  
#include<time.h>
int binarySearch(int arr[], int size, int element){
    int low, mid, high;
    low = 0;
    high = size-1;
    // Keep searching until low <= high
    while(low<=high){
        mid = (low + high)/2;
        if(arr[mid] == element){
            return mid;
        }
        if(arr[mid]<element){
            low = mid+1;
        }
        else{
            high = mid -1;
        }
    } 
    return -1;
}
int main(){
    double time_spent = 0.0;
    clock_t begin = clock();
    int arr[10000];
    for (int i = 0; i < 10000; i++)
    {
        arr[i]=i;
    }
    int size = sizeof(arr)/sizeof(int);
    int element = 200;
    int searchIndex = binarySearch(arr, size, element);
    printf("The element %d was found at index %d \n", element, searchIndex);
    clock_t end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("The elapsed time is %f seconds", time_spent);
    return 0;
}