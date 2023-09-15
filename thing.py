from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "awi4iwZztiuw5Ce7U_0HS-MQ8dtI7zMInDnnIeDY8kpLcK7FZhKm4CqlujwZuRo5Ol9zbw.",
    "__Secure-1PSIDTS": "sidts-CjEBSAxbGWDY_K0OSUUPfYpiMtSsD9PRSQHpYueLOU9IBEQxf8D7lPVzoe-x-2r7T8IpEAA",
    "__Secure-1PSIDCC": "APoG2W_akEsNA8Xjzu-icq_aDg7a3R_qCv_YIqIPP6qm1z_HCaAELB6WJVQeoB1FO8AxGIVN4g"
}

bard = BardCookies(cookie_dict=cookie_dict)


print(bard.get_answer(str(input("Please enter your prompt: "))))