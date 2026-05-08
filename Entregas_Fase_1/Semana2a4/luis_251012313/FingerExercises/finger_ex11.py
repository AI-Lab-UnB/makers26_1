def remove_and_sort(Lin, k):
    if len(Lin) < k:
        Lin.clear();
        return;

    for i in range(k):
        del Lin[0];
    Lin.sort();

L = [1, 6, 3];
k = 1;

remove_and_sort(L, k);
print(L);