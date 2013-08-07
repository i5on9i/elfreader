
__author__ = 'namh'
__version__ = '1.0.0'
__contact__ = 'gaedduck@gmail.com'


import mmap
import struct



class Header:
    def __init__(self, format, data):
        self.__keys__ = []

        self.__format__ = format
        sutruct_format = self.__get_struct_format__();
        self.__generate_keys__(format)

        self.__keys_in_dict__ = {}

        unpacked_data = struct.unpack(sutruct_format, data)

        self.__keys_in_dict__ = {}
        for i in xrange(len(unpacked_data)):
                #self.values[key] = self.__unpacked_data_elms__[i]
                setattr(self, self.__keys__[i], unpacked_data[i])
                self.__keys_in_dict__[self.__keys__[i]] = unpacked_data[i]


    def __get_struct_format__(self):
        f = ''
        format = self.__format__
        for e in format[1]:
            size = e.split(',')[0]
            f += size
        return f

    def __generate_keys__(self, format):
        '''
            make __keys__ with element name

            NOTICE
            This function does not care of union
        '''
        for e in format[1]:
            key = e.split(',')[1]
            self.__keys__.append(key)

    def dict(self):
        return self.__keys_in_dict__;




class ELF:
    __IMAGE_ELF_HEADER_format__ = ('ELF_HEADER',
        ('16s,e_ident', 'H,e_type', 'H,e_machine',
        'L,e_version', 'L,e_entry', 'L,e_phoff',
        'L,e_shoff', 'L,e_flags', 'H,e_hsize', 'H,e_phentsize',
        'H,e_phnum', 'H,e_shentsize', 'H,e_shnum', 'H,e_shstrndx',
        ))


    def __init__(self, fname):

        self.__keys__ = []

        self.__parse__(fname)





    def __parse__(self, fname):
        with open(fname, 'r+b') as fd:
            self.__data__ = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ)

            elf_header_data = self.__data__[:52]
            self.elf_header = Header(self.__IMAGE_ELF_HEADER_format__, elf_header_data)



    def __str__(self):
        '''
            print in json type
        '''
        import json
        return json.dumps(self.elf_header.dict())





if __name__ == '__main__':
     # elf = ELF('./test.o')
    elf = ELF('./a.out')
    print elf.elf_header.e_ident
    print elf

