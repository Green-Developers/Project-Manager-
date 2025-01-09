class ParenthesesChecker:
    def __init__(self, layers):
        self.layers = layers

    #چک میکند ایا لایه ای با عمق ان وجود دارد؟
    def has_layer(self, n):
        return self._check_layer_depth(self.layers, n)


    #بر اساس لیستی که بهش از ایندکس های تو دراو داده میشه ایندکس مربوطه را پیدا میکند
    def peek_layer(self, list_n):
        layer = self._get_layer(self.layers, list_n)
        return layer if layer is not None else []


    #برگرداندن عمق عمیق ترین لایه تو در تو
    def size_layer(self):
        return self._get_max_depth(self.layers)

    def pop_layer(self, list_n):
        return self._pop_layer(self.layers, list_n)


    #افزودن یک مقدار مشخص به انتهای یک لایه خاص
    def push_in_layer(self, item, layer):
        target_layer = self._get_layer(self.layers, layer)
        if target_layer is not None:
            target_layer.append(item)

    # یک لایه به انتهای لایه مشخص شده اضافه میکند
    def push_new_layer(self, type, layer):
        target_layer = self._get_layer(self.layers, layer)
        if target_layer is not None:
            target_layer.append(type)

    def _check_layer_depth(self, layers, depth):
        if depth == 0:
            return True
        if not isinstance(layers, list):
            return False
        return any(self._check_layer_depth(layer, depth - 1) for layer in layers)

    def _get_layer(self, layers, indices):
        for index in indices:
            if isinstance(layers, list) and index < len(layers):
                layers = layers[index]
            else:
                return None
        return layers

    def _get_max_depth(self, layers, depth=0):
        if not isinstance(layers, list):
            return depth
        return max(self._get_max_depth(layer, depth + 1) for layer in layers)

    def _pop_layer(self, layers, indices):
        for index in indices[:-1]:
            if isinstance(layers, list) and index < len(layers):
                layers = layers[index]
            else:
                return None
        if isinstance(layers, list) and indices[-1] < len(layers):
            return layers.pop(indices[-1])
        return None

# Example Usage
layers = [1, 2, [3, 4, 5], 6, [11, 12], [7, [8, 0, 9], 10]]
checker = ParenthesesChecker(layers)
print(checker.has_layer(4))  # ایا لایه ای با عمق ۴ وجود دارد؟
print(checker.peek_layer([2, 1]))  #ایندکس ۲ ازlayers = [3, 4, 5]
                                    #و ایندکس ۱ از ان  = 4     

checker.push_in_layer(7, [2]) #  عدد ۷ را به انتهای ایندکس ۲ اضافه میکند
print(checker.layers)
print(checker.pop_layer([1])) #ایندکس 1در لایه ها حذف میشه و مقدارش چاپ میشه
print(checker.layers)
print(checker.pop_layer([1,1]))#به ترتیب وارد عمق لایه ها میشود وه ایندکس مربوته را پیدا و حذف میکنه
print(checker.layers)
print(checker.size_layer())#برگرداندن عمق عمیق ترین لایه تو در تو
print(checker.push_new_layer([],[4, 1])) #یک لایه جدید به انتهای ایندکس ۴ ایندکس اولش اضافه کرد
print(checker.layers)