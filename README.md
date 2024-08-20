### Завдання ([Task](task.py))

Python має дві вбудовані функції сортування: sorted і sort. Функції сортування Python використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.

Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних. Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. Для заміру часу виконання алгоритмів використовуйте модуль timeit.

Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.


Згідно з даними конспекту курсу ми маємо наступне:

#### Merge Sort:
 - Часова складність: O(n log n)
 - Просторова складність: O(n)


#### Insertion Sort:
 - Часова складність: O(n²) у гіршому випадку, O(n) у найкращому випадку (майже відсортовані дані).
 - Просторова складність: O(1)

### Timsort:
 - Часова складність: O(n log n) у гіршому випадку, O(n) у найкращому випадку.
 - Просторова складність: O(n)


Після проведення тестування, ([Task](task.py)) отримаємо наступний результат:

![result](result.png "result")

**Size** - 
**Merge Sort** - 
**Insertion Sort** - 
**Timesort** - 

