# Lab 5 Reflection and Observations

* name of team member 1
* Lorenz Alvin Tubo
* name of team member 2
* Abdullah
* name of team member 3
* Fausto Javier Zaruma

## Heap Insertion

### Picture of heap created with 10 values
![8010206f-5f31-4e09-9789-ac08c1b668df](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/5549bd05-0eae-4b39-8db9-ad95917f274b)



### Pictures of adding 11th value to heap
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/3e882067-bd0a-4360-a567-a3eff2e3f785)


## Heap Removal

### Picture after 1 value was removed from heap
![b86aadee-3ad3-48fe-a904-bf66a4d13b93](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/3763093f-eca2-4eaa-a280-aaa97fd18981)



### Picture after 2 value was removed from heap
![799c2bcc-130d-4e14-a894-ed40a881c352](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/bde3cdc3-dc7a-40b0-b5dc-d55124d776df)



### Picture after 3 value was removed from heap
We Forgot to take a photo of the 3rd removal but judging from the previous removal, It is safe to assume that 7 would be removed next and will be replaced by 8.
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/a4791ab0-db98-401f-886d-a0f877e69d12)


### Values removed (in order removed):
5, 6, 7 Due to the fact that in a min heap the parent node must always be less than the child node the root node must infact be the node with the least value. 

## Array representation of heap
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/4247b08e-8abd-4af0-bd06-d1eb001f5406)


### Picture of heap
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/d9c18436-e8b3-48e4-8e14-fe7e932d696a)

### Array representation of heap
[7,8,9,15,21,10,12,57]

## Creating a heap from array
Random Array = [ 5, 12, 39, 6, 57, 15, 7, 10, 21, 8, 9 ]
### Photograph of your array and heap
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/7fbe732a-3c77-497f-9e29-b9be1c0440b2)


* What number is the first non-leaf node starting from bottom?
* 57
* What index is that node at?
* index 4.


### Photograph of heap created by Heapify
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/6f317b84-d04b-4a94-9853-da9faa9a52e9)



## HeapSort

Initial questions (do first):
how many values are in your array?
11
what is index of last value in array?
10

After doing 1 removal operation
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/59d9b5e9-8b6e-4bbf-a58f-3cc831746174)

* what was the first value removed? How does this number compare with others in heap (biggest? smallest?)
* Biggest since the tree has become a max heap tree the root node or highiest priority node contains the highiest value.
* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
* 10 values in the array index 9 contains the last index of the heap.

After doing 2 removal operations:
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/0ff68df0-03c1-46f6-980a-c945d198c0d4)

* Perform another remove from the heap and adjust the array to match
* What was the second value removed and how does it compare with others still in heap?
* Biggest since the tree is a max heap the node that replaced the previous node that was remove contains the highest value in the current tree.
* Look at your heap portion of the array after you did this removal.. how many values are in what is the index of the bottom right most value in heap?
* 9 values in the heap index 8 contains the last index of the heap.
* Are there any open spots in the array that is not part of the heap and not holding anything useful?
* No because the array that represents our heap contains the previous values that have been removed from the heap.

After doing 3 removal operations:
![image](https://github.com/seneca-dsa456/labs-ltubo/assets/107896556/9d36b30c-27e7-4127-b807-a0dbd9828158)


* Perform another remove from the heap and adjust the array to match
* What was the second value removed and how does it compare with others still in heap?
* 21 it was the biggest value in the current heap.
* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
* 8 values index 7 contains the last value in the heap.
* Are there any open spots in the array that is not part of the heap and not holding anything useful?
* No because the array that represents our heap contains the previous values that have been removed from the heap.


## Reflection

This last part is to be completed individually.

Write a short paragraph about what you learned from this lab.
* Discuss what you learned about heaps and heap sort.
* I personally think the most important aspect of heaps and heap sort is that they are effecient in priority queue operations, they are good at efficiently sorting algorithms also their ability to work on individual elements, making them suitable for scenarious with memory constraints.
* What was the most surprising thing you learned about heaps?
One suprising realization is that when a max-heap is created from the array and k "delete max" operations are performed, the kth largest element is found in O(n + k log n) time, which is more efficient than sorting the entire array. If you have a large dataset and only need a few elements, this is especially useful.

