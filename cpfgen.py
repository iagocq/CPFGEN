#!/usr/bin/python3

# CPFGEN simply creates CPFs and CNPJs.
# Copyright (c) 2017 Iagoq
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from random import randint


def gen_cpf_validators(cpf):
    v1, v2 = (0, 0)
    for i, d in enumerate(cpf[::-1]):
        v1 += d * (9 - i % 10)
        v2 += d * (9 - (i + 1) % 10)
    v1 = v1 % 11 % 10
    v2 += v1 * 9
    v2 = v2 % 11 % 10
    return (v1, v2)


def gen_cpf():
    cpf = [randint(0, 9) for _ in range(9)]
    v1, v2 = gen_cpf_validators(cpf)
    cpf = ''.join([str(_) for _ in cpf]) + str(v1) + str(v2)
    if not is_valid_cpf(cpf):
        return gen_cpf()
    return cpf


def is_valid_cpf(cpf):
    if len(cpf) < 11:
        return False
    try:
        if isinstance(cpf, str):
            cpf = cpf.replace('.', '').replace('-', '')
            cpf = [int(_) for _ in cpf]
            if len(cpf) < 11:
                return False
    except ValueError:
        return False
    v1, v2 = gen_cpf_validators(cpf[:len(cpf) - 2])
    return v1 == cpf[9] and v2 == cpf[10]


def gen_cnpj_validators(cnpj):
    v1, v2 = (0, 0)
    v1 = 5 * cnpj[0] + 4 * cnpj[1] + 3 * cnpj[2] + 2 * cnpj[3]
    v1 += 9 * cnpj[4] + 8 * cnpj[5] + 7 * cnpj[6] + 6 * cnpj[7]
    v1 += 5 * cnpj[8] + 4 * cnpj[9] + 3 * cnpj[10] + 2 * cnpj[11]
    v1 = 11 - v1 % 11
    v1 = 0 if v1 >= 10 else v1

    v2 = 6 * cnpj[0] + 5 * cnpj[1] + 4 * cnpj[2] + 3 * cnpj[3]
    v2 += 2 * cnpj[4] + 9 * cnpj[5] + 8 * cnpj[6] + 7 * cnpj[7]
    v2 += 6 * cnpj[8] + 5 * cnpj[9] + 4 * cnpj[10] + 3 * cnpj[11]
    v2 += 2 * v1
    v2 = 11 - v2 % 11
    v2 = 0 if v2 >= 10 else v2
    return (v1, v2)


def gen_cnpj():
    cnpj = ([randint(0, 9) for _ in range(12)])
    v1, v2 = gen_cnpj_validators(cnpj)
    cnpj = ''.join([str(_) for _ in cnpj]) + str(v1) + str(v2)
    if not is_valid_cnpj(cnpj):
        return gen_cnpj()
    return cnpj


def is_valid_cnpj(cnpj):
    if len(cnpj) < 14:
        return False
    try:
        if isinstance(cnpj, str):
            cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
            cnpj = [int(_) for _ in cnpj]
            if len(cnpj) < 14:
                return False
    except ValueError:
        return False
    v1, v2 = gen_cnpj_validators(cnpj)
    return v1 == cnpj[12] and v2 == cnpj[13]


def main():
    cpf = gen_cpf()
    cnpj = gen_cnpj()
    print('CPF:  ' + cpf + '    |   {}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:11]))
    print('CNPJ: ' + cnpj + ' |   {}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14]))


if __name__ == '__main__':
    main()
