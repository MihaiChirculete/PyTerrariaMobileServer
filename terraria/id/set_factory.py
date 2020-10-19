import threading


class SetFactory:
    def __init__(self, size):
        self._size = size
        self._int_buffer_cache = []  # private Queue<int[]> _intBufferCache = new Queue<int[]>();
        self._bool_buffer_cache = []  # private Queue<int[]> _intBufferCache = new Queue<int[]>();
        self._queue_lock = object()

    def get_bool_buffer(self):
        self._queue_lock = threading.Lock()

        with self._queue_lock:
            if len(self._bool_buffer_cache) == 0:
                return [None] * self._size  # return new bool[_size];

            # port of: return _boolBufferCache.Dequeue();
            x = self._bool_buffer_cache[0]
            del self._bool_buffer_cache[0]
            return x

    def get_int_buffer(self):
        self._queue_lock = threading.Lock()

        with self._queue_lock:
            if len(self._int_buffer_cache) == 0:  # original used _bool_buffer_cache but that didnt make any sense
                return [None] * self._size  # return new int[_size];

            # port of: return _intBufferCache.Dequeue();
            x = self._int_buffer_cache[0]
            del self._int_buffer_cache[0]
            return x

    def recycle(self, buffer):
        self._queue_lock = threading.Lock()

        with self._queue_lock:
            if isinstance(buffer[0], bool):  # if (typeof(T).Equals(typeof(bool)))
                self._bool_buffer_cache.extend(buffer)
            elif isinstance(buffer[0], int):  # else if (typeof(T).Equals(typeof(int)))
                self._int_buffer_cache.extend(buffer)

    def create_bool_set(self, *types, default_state=False):
        types_list = list(types)
        bool_buffer = self.get_bool_buffer()

        for i in range(len(bool_buffer)):
            bool_buffer[i] = default_state

        for j in range(len(types_list)):
            bool_buffer[types_list[j]] = not default_state

        return bool_buffer

    def create_int_set(self, default_state, *inputs):
        inputs_list = list(inputs)

        if len(inputs_list) % 2 != 0:
            raise Exception('You have a bad length for inputs on CreateArraySet')

        int_buffer = self.get_int_buffer()

        for i in range(len(int_buffer)):
            int_buffer[i] = default_state

        for j in range(len(inputs_list), step=2):
            int_buffer[inputs_list[j]] = inputs_list[j + 1]

        return int_buffer

    def create_custom_set(self, default_state, *inputs):
        inputs_list = list(inputs)

        if len(inputs_list) % 2 != 0:
            raise Exception("You have a bad length for inputs on CreateCustomSet")

        array = [None] * self._size  # T[] array = new T[_size];

        for i in range(len(array)):
            array[i] = default_state

        for j in range(len(inputs_list), step=2):
            array[inputs_list[j]] = inputs_list[j + 1]

        return array
