import sys

def check_value(data, args):
    for i in range(len(args)-1):
        if data == args[i][0]:
            print(args[i][1])
            return True
    print(args[-1])
    return False

with open("a.out", "rb") as f:
    byte = f.read()

    if byte[:4] != '\x7fELF':
        print("Not elf file")
        sys.exit()
    else:
        print("[+] Format: ELF (Executable and Linkable Format)")
    print("[+] E_IDENT: ")
    args = [('\x00', "\t[+] EI_CLASS: Invalid class"),
            ('\x01', "\t[+] EI_CLASS: 32-bit objects"),
            ('\x02', "\t[+] EI_CLASS: 64-bit objects"),
            "\t[+] EI_CLASS: Invalid value"]

    check_value(byte[4:5], args)

    args = [('\x00', "\t[+] EI_DATA: Invalid data encoding"),
            ('\x01', "\t[+] EI_DATA: ELFDATA2LSB"),
            ('\x02', "\t[+] EI_DATA: ELFDATA2MSB"),
            "\t[+] EI_DATA: Invalid value"]

    check_value(byte[5:6], args)

    args = [('\x00', "\t[+] EI_VERSION: Invalid version"),
            ('\x01', "\t[+] EI_VERSION: Current version (1)"),
            "\t[+] EI_VERSION: Invalid value"]

    check_value(byte[6:7], args)

    args = [('\x00\x00', "[+] E_TYPE: No file type"),
            ('\x01\x00', "[+] E_TYPE: Relocatable file"),
            ('\x02\x00', "[+] E_TYPE: Executable file"),
            ('\x03\x00', "[+] E_TYPE: Shared object file"),
            ('\x04\x00', "[+] E_TYPE: Core file"),
            ('\xff\x00', "[+] E_TYPE: Processor-specific"),
            ('\xff\xff', "[+] E_TYPE: Procesor-specific"),
            "[+] E_TYPE: Invalid value"]

    check_value(byte[16:18], args)

    args = [('\x00\x00', "[+] E_MACHINE: No machine"),
            ('\x01\x00', "[+] E_MACHINE: AT&T WE 32100"),
            ('\x02\x00', "[+] E_MACHINE: SPARC"),
            ('\x03\x00', "[+] E_MACHINE: Intel 80386"),
            ('\x04\x00', "[+] E_MACHINE: Motorola 68000"),
            ('\x05\x00', "[+] E_MACHINE: Motorola 88000"),
            ('\x07\x00', "[+] E_MACHINE: Intel 80860"),
            ('\x08\x00', "[+] E_MACHINE: MIPS RS3000"),
            "[+] E_MACHINE: Invalid value"]

    check_value(byte[18:20], args)
