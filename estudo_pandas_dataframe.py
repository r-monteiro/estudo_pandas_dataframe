# -*- coding: utf-8 -*-
"""PANDAS - DATAFRAMES.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BLhXpCaqt4zwyGeYQre_W_2wILGSYbfo

# **CRIANDO UM DATAFRAME**

![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB1cAAABpCAMAAABRXVoAAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABjUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGZodN4AAAAgdFJOUwAIEBggKDA4QEhQWGBocHiAh4+Xn6evt7/Hz9ff5+/3v+H4wgAAAAlwSFlzAAAXEQAAFxEByibzPwAAHS9JREFUeF7tnYl24yoMhpukS6ar2+l00j3v/5QXCWEERjZecttM/++ce8eujZF+yYDxkhMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgBKrm+ZmJcsAgCPnV3N3Kos/nLOn3d9fsgwWAqLWcbvf789kOeELBPyKmK3+7vef57JyCOY5Nb70t0j85Y1Y/93t7mX54Ewx//Jjv3+U5RoOFafn/f5FFg/G9u/n/vXhuw/Hr13TNiYioAKIWsXqfb9/luWULxBQV7nZbmWpzND2WhpX566nhZhdzzwdx5dePm4TJFjeiK074pssLxV7kwnmb9yJ9DnGLF3Hkg7RQPlSlhfhutlRX/23uZA/cKPhaGT1u7JoEl42CYcciX9rlhG1VXN7kFP564N15WS6luWU5ZvGQVSVvz73+9ee7m5oey2n7jjvG1kpML+eeTqOL7143KZIsHzyqH51qdjbTDD/0RW5leUqVB2LOrR2B/srywtw/ebsFF7k+vrCry5Yy0FYMglvvMstB58S+K4sImqq5u6upwGewjcI1st+/1E+o5dvGgdRVVIzte8Zygxtr4VmgfsOM7+eeTqOL7143KZIsHzyqH51qdjbjDefzHuS5TpUHcs6REdbaoS+fiXTIv6SlZx17Hill/V2+3VXdksmoWsnEsLUyY9jEVFzNT8fFu1Zvz5YdIY8yHLG8k3jICOamoWaIrpc773KmF/PPB3Hl148blMkWD55vne/unL9z9taVupQdSzrEF1NLqV93kL5qa0zvzJcyW/a7eOretaaKJ65q/sasXbkieK7X6sfjEXO7FxNlyQ1ty6OJ1h0Rre3TVKWzMpKVJV3bvGzZxAztL0OulHUf5Uxv555iTi+9CKJr5kiweJG6H51wKAFknK0+Y2zqPj0n42qY5lkbnF9/Ocys8r08EGC3DL6Q8sV/aWfQy7fZzo8NVGktKq47uam+rvfT/5fWOTMbtU83W7vn92Ko+ImytEEa/Wx37/Lcs6SWVmJrvJ64Hbz0PYqHvb7l4EWaHY98xJxfOlFEj9hggTLG6H61QGDFkjKseZvXFd+Jcu16DoWSeaWe3fksdYUOXUHIu4vTlbba2r/Qhd5fnW7rbg8R7/6z7HImZ2qee571uEr1qMJ1i9ngCXSkllZySIxG8Ovphk3eTeBeU6NL/2/i1hieSN0v9rPF/Sr67tm9Cszh4sTCfBHlmdB19GOtjN9GjtZjX71n2ORtM3V5HmRj8HXro8mWDQNbI1sl8zKSg7X1Hwh85waX/pbiLi8EZRq37ZfncLh6qBZqEUmgnm6d/8qaxNAv/rPsUjadtTkjnXwub9jCRadgHvrgm3JrKzk/2jO/nfmOTW+9LcQcXkj0K/W8+QOvcREMLVPRS3Xl01zK/eTN9eNv1hf3+x2u4frdkL7Yrv177nebx3txcj57ZPbb/fQxO52c9U0zWV7f/r8pmlu2rX11SPt/3hd+xWpCzKIWrVc4dOtq+Zum4w4SslS2s9oqtfer1P9kmSpuOx3cnrZ3MQJ9M1lc116umXrBChuqGa99bfr19u75rJzi6HPws0vF4qu1KNEJbYuRa6sZwa6anKqaUOPOVhkZ/5RiINkZT/FKlf5A/pnv9xRWy+7289dIC8zx/uTpUfTqH1VPQVMHYuRyBmdxn31WRb3pr5CSTD17Os6fZbqei4HNqFUC/1qFpPMj+lJOT1mMyXqJFmW7B7Dhm4Y6f2937I8B3/f6zO3I2zwprzQouvFZdK4bdHkoeGAj93mXr0O+xbuqPFjw22zSjen2mc4180nrxJ3/k/Mais9R86N78s/f6/TKJ7et68MPYhD8nkL4dPHqrAfUW6qyUfnun+8izeXi8t+F/7x6o+G83D927v2lOob/rz/mP55Malv8+gP9aZnDHotPPNTFPvnNHFHiMps5DD7F3fMAl01z2nvfyVY9GmW9Pw7UFb2Ua6SHupUXf5ZeOD/r9zhybavfwdr3u5j49mXLL2aRu2r6uli6Vh32oxN4/76yhYPpX5ESTDt7Cs5TakXb6isqKHuv0Op+tUkJqkfc5JyRsxmSpQlWSfZCcOGYhjpTZsl3oWX/k4pIfjO0VvHy9dr39UyT5xn5J+G/vaLJsgUchdYvjMh84DcUctTLGeqG9Zi0ntNn6WEeZBd9/v3rVJ4Rc9ytbz7g4fHsgRyp7gfUW6qKSmvZbqcqrKK+/3uJIIusE6hizZVX3SOXCiPnysGvUV8fddR7XZI0m/hbWvhh76TPkZU4ro9jHFWF9Sk/JHz++iDRXUkjzcfKit7MKok5+K0X3QyDATS7Vf6fH1tp5DsZOnXNGpfV08HwylHzWkzNo376rMsHkz9iJLAFtQxyukN2dW+V0bXOgMPZmdWhJhkfsxIyjkxmymRdqiU7A7DhnIY125tiRusNPgh/uZOe2O8Z7zctCMXgtsU8k9Df0v2IiQaNHHtYA8uedFPOJzp7HV8BENIscJrifSx75ZPOo1FYfkCz9vOH/Ddi5MenY5d3s/R01SH/HJVWcV5P35LWXjkb2wFYuxF8rfdjjd/dGcnVrdNzm0n1FyfvzgQgu29FuoS8ZvpI0X1w8T9+263o3B3RXMU1OS6/aj36INFp4RqVA+VlT2pYFZJzgUPVnLaCTypobe3U1By2n6GaQ87WXo1VdrX1ZNhOlVx2oyOgqOnPsvi4dSPKAlsQUc7zd5Is0ofk/SzinaqZFbIYseP6qTMmBezmRKp4sVkN22wwkij67ba6fDkHJF/D6fTr6awxr5/bPmgfWV5317cSjTYD7nG9perbD1dlRLPD49SInzDhueK88l+ken19uzktJFEEIXdgOb9gUeVax7b+OOcbrdU4oXu//qZ+PJ+DruppqA+327vnt1mqzgH2P23255s/EiXBk/vV6vVlt1tB3v0nZr9Hxabb06/dbK1nW5XdGZRQn3P1+uTi3uuUFKmz0Iy5eVqdbLlPG2HdCNF9RH8zYafP5ZfSy2oyenidSgf93iCRcNabnqEQ2VlTyqYVbJzfpEO66q53JystjSMYMX0dj79P+4u3FXQJY8zPt0iYSeLYWlH+7p6MkynKk6bCWncU59p8XDqR5QEtqDjnaaWUppVOpI/kJ0qmRWy2PFjxNmXMC9mMyVSxYvJbtpghZHqvZHlOXDOeB5ZTKHYr378eSB7CDJl9SCjgP2r6/h3PEBw/eTnn0u6KtnIoWVYz15zk+W7Yz8l7Icn75yzV3wsmdlnxbr9Kt8FePEXPae+TxaFb978bTKC6vqUZT6QOo65n91UO0KqmMVlPx+hc68Kzy+6pCQ7w6Q9OxDmbHmLvqfMyNx8QpthAalPUn1LFcqU+4CFUh2N+cKHSkaLSt1KexfitN1DU1CTmyo/ijz2YFEK8zDSc7CstFPBrpKOLE0NK+79cns9+wZDbefW5Y1bTgdPP4nrolAhWQY0bbWvqyfFdsqMhGJ8FOwSpsUVqR9REtiCjneaM5bPfOo13n1RO1UyK/xi0Q/aXHP2acabnzBTIlW8mOyWDWYYyc9OYzsBnq0P/Il3lkr96iN5JhfqIf/8tjit8/stvi/u+2AZDEhFL6sVF/HdJ7vdXnjzqCR0D7ypM3KgqYn3YOWaKwiWKPgtCIlJniyaZD9qqh95sMbIn32wy5/J08X9fuEOuB9SBMt4zCT7kY/xaNQ+S1pEsmkARt1a9/j62q6FzvzC97xsC+k7J0He0aLSXILxHEKg0PGt6MDdU+sYg0Vyq5fTDpaVdirYVdKRxUxqa9VHoa74zFTb6fAqa9h1f1mWKqSTRdPVVGlfVU+K7VTFaTMhCnYJ0+KK1I8oCWxBJzhNbTBNkq6pjZTJFdqc46vLrPCLRT9oc83Zp5kXs7kSqeLFZLdsMMNI0o77FQCD8/Zq1PHZnjyFflWaSXarlT/vVzV+aiLMHpCLjlv/r/8rDwRbPzh27TBifRnfxGmhyuNwgiUunDs8UxJO3J5kSfajploh180cbBkSdlDFeb+20+C1MHbyfsl+ZLGaF6ARVClbB+Ea4sTMirKw22fZFnJvoiI6SlTKyoHPkpQuKKkVyP/mOMJgUQ4rM0cLWO+ohV0lHdk3HpwUao7LE7fzQWIO+QD59VQhnSwJuaZa+6p6UmynaHHotLFLJyib++srWlyR+hElgS1ovxFFp/nu2bPvSoY7gcwKv1j0gzaPTcoJ5mtmShSLl5PdssEMI/VIlgTj2JBiLcH8br8acpQGD3G03tev+l4zDBfk2vSd/5GxoH/Ooe3MSYXybIPAlzwqulRDsEujX+/tSxa9X9ZUi+8cbL/YRRVX+eHYUKkwwPI56YeV5ID+rCxN5w81oUWoPn0gmjYpJIppIQ96fLDHi0ruDXw7utSvUq4UWucjDBaNaqOZh8xKg54qo3M0M9adxIjb6cWGZDudjn5YmyqkkiUl0zTRvqqeBNspOxKR8VGwS9gWV6R+RKloCjrJaRb7ml6y6Ma3Q9GKoh+0eWRSTjJfUTSOqWqgYplisps2mGGkY8/4TFLCpe8cPdLwdfvVcM5QV+9ckLXhfrUNFE+mCDIsoWApyXxrGZu4DpTvWielcAKNdYJNfcmi98uban+xnAU7RRXP9qPBU/SD3PT7kQNxXsKPOMviDZDbRaOdgpe2hSSdH+tOEJWi/lGYGIxY/Wocj7YcYbBoKUp0yKw06KkyOkdX1d3uK26nEzLZzm/D5ZPFREyWFFvTynoSbKfsSETGR8Eu0WPxcOpHlCamoNOcJife6eqrc4XWpWxFyQ/aPDIpp5kfmSeRKlNMdtsGK4wUeWXETK74SpGRH+2hesv9KrnikDW/LdXr9KZp/sgjzDpQsZLwyHb8i0IPejOoT9fiKYWF9Za+rUHHDTaVk6W7HzXV6paddPZZsAOd4tl+JEtsqmNO0gz/izwGT5S6nypyu0iZxM4hC6MsE0Slwu5oN8aUq6PkGJUJajNHGyzaJ0p0yKw06KkyOkcXWbpV8cTtnXtJ/A4jK5Ep1LV2SNPKehJsp2pOm/FRsEsMKOMc60n9iNIkk4dWh86+Pqc3fvJPfxPBpGwFLeZ+RKs0vUk5L2aWcUQ0pieysUwx2W0bqGDuPkF/75sxHcu2nQ32s4nT+9Vr3522xEBJSUcYZdGVQoeefpWuyrR46bmzudFVB5uo1jRZyvsNxj1QLJ7tZzXV/pZzSrfSCnK7WFtZrrKQVr0sU0SVt7c/H7uto6egJs+3tlNJRx2stF89ZFYa9FQZnUutDKTbk9ucPOHGp1+mUGptjaaV9STYTtWcNuOjYJfos3gw9SNKE1PQiU7Tbs6Imhlpw4qCH9GqwGBSzouZaZwjGtMT2VimmOw9NhhhpAO27egi+NdcwhX35H6V/EtQ56PU0Par3NJ26LljQONILZ5S+GSV1RxsivHxWPtVNtVG8Ww/q6mmiYicbgNTQW4XD6j9Yp2FUZYpop5c0PiVMD5KV1CTBo9BlCMPFu0TJTtkVhr0VBmdo0P2idTd7v7g78pkCmlr6zStrCfBdqrmtBkfBbtEr8VDqR9RmpiCTnSaH9PZvw5ZQFhWdP2IVnkqknJezGzjtDE9kY1luiFz9NlQDuOy88BM+ORMexsh2DCmX80i4YiBittkHrjUr/Z8/NMrbIxc/Cc5Pulz/70zbuZ+dU21VTzbz2qqyYEnmbwUOg89b/mx6ISP9ksFgdwuugHkR0SVFkZZpojq2Pqb4/vX4oxYQU1Kcnnp89iDRVuimYfLSjMVeqqMzpHg3aeN0u3J2cZXZTyszRRS1lZqWllPgu2UHYnI+CjYJQYs7k/9iNLEFHSi0zTt6YiPK9itRo8VmR/RKsZMXsVE81t6jHOrQxKpMsVk77ehFEY69lLPLQVYRhmWTexX5cL75Ya+2EE2qkDxi7uC5INfqX28zh9R31JQCpPxH2G6PLaNOj6MuV9dU20Vz/azmmoyeOgxfXo1OaeTMblddDHolam0MMoyRVRm4z9+ktyICnTV5NkK2ffYg0VpHs2cImCdo2Yq9FQZnSMru8FJtyf+0aSHH/lkCilrKzWtrCfBdoqWhk6bHkkMm+0Sgxb3pX5EaWIKahtBS5bToS0NX9HpazVsK3I/olWMmbyKaeZHbOOiMXYdqkwx2Yds6IaRSigJFkHeMOUefWK/6kcA4jTZqKykttBlgv+/H/v5MdbAOwUKqrv8ZBg/Zh1M7GnB7P2qmmqzeLaf1VSnxpShQVZO5yI+q4/vQXAG1VoYLaGlsaIKa453aVzUVZNPfD+CPvpgkURxVDtFwDpHzVSwq1TO0ZyWbo886fbEP9rkHxCJOzG06ves1bSyngT6c9mpWL+NXdqy2S5RYbGd+hEqJZqoRYJWfQW2EXGfDiu6euRbn+0OdqthW0FoP9Ia7eRVTDJfYRsXy9t1qDLFZI/HsMjDyFe4srwUdCnt4AHKuH61fWCZO8rwgwDkf/SLb6/t38l/h38qgEZEpbkqC3puWjWBSmGaF4l65C1YPCXs/aqaarN4tp/VVNO4V6dIiU3TpTNpltXHSvJpVGshrfrQTBG1hR53K7110FGTL1dl/v/og0W5HC9fDpeVZirYVSrn6N7Ah755xKTbO29p+uF9phCt+mSp1bSyngTbqZrTZnwU7BJVFlupH1GamIJOcpouzp75Odk2oexWw7bCE/2gzTVnn2JezPqMo9UhiVSZYrLX2JCGcZnvGJ59PsbskWe3/Ti8tl/1PWO4nGIFWnHI/7Zf9Z8vdBcs/sFj/zqPH2R1Xuc1WVPjHO8prOmYXmEKe7yo00lAgsdw2ftVNdVm8Ww/q6nmme/OzdIJcBTihT7fqeYqai2kVR+aKaK2UASTJyeFjpr04YrwvJp93CMJFp2v8XbbIbPSwK5SOcdWdl5wjNs5adR2/nKLX88UolWfLKalWYnKehJ6nKIjDJw246Ngl6iy2Er9iNLEFHSK0/wjJu4ai86p98HG07bCE/2YkJTzYjZbolimnOz0xwEb0jBSf1ZIzZG4i8fPR3nM7ZzmFhy+uSLba/pVf437JpPw/ik1eeX73PfT0q/6SWY3GqLpBQePhGT5TxxnnLV9RfF3zam69ucG+YNWonAyzjgli0MS8DnSVmDvV9VUm8Wz/WhLsammA8Qh4XQ4CvH3aemw/mKw1kJaldBMELWFsjLk4YX/GQwmU3PF3arU13PcYwkWzcvE34k7YFZamFVq52iOS9l/kz/qy9tbI/gUlSdMM4Vo1QevVtPKelJsp+xIRMZHwa6vxmKd+mfbrTSBGiWBKegUpyn7qSvgOSDZ2ca2whP9mJKU82I2VyJVppjsFTboMPoPVoaebjr+ivJ199Dc+8tIZ6XPD5Kxpl+lGQnH28PDK/nHPu//uGOswg/Hem3ks/s0diABHNwGy/LrJa2tftHP00vbXP5dc+6IZULm1FfmFSZPwtcmOAdiEtBK21vb+1U11WbxbD/aVGyqWYeHkCOOs+qL9QQfhfCrkBxHnxy1FtKqpO1oURs5pIsSpY0MzEjAdnybqLm65SFWO7S2g3AswaL648l4wKy0MKvUzvFOj3Lczc4Py/V2OkXld0L8LfowuM8UolWfLLWaVtaTYjtVc9qMj4Jdn2lxOfVpRrYw36gkMAWd4DSZ47/EzBcrQ91A0YqyH3S4kUk5L2ZzJVJleKc82S0byu67TpsOEsI+HX/PUxPeNGYdK/pVnuMX3CqNDxzvO2p4PF4bv4GHDiyA3GSWn2XVSD1cjX662sPd/6Prb9d3TjJSzSvMM9BPrMgl/VUlARWh354/u3P62vtVNdVm8Ww/kqzYVPtT4VkCeX73GoeEo5Ao7J/OqNsiFeUUqLWQViVtR4v6tn++5to2dBkqdzV4IqZtXEjNnb/LE4Zsb+3V7PEHKxnLHzIrTawqE+d42PpMl1LbB5cjvIfezmfl2zXl0JZnFMLYPlOIVn2y1GpaWU+G6VTVaTM+CnZ9lsXF1OdbkYUXh5QEpqDjnea+wnvAzy8NvcRatKLsB5kyNinnxWymRLpMKdktG8ru5zPhk2HpEsJopbZflRusjFsL39fycDRYG+lL/ZhPLlJ5RR5jUkg9XE3QNXLOx9x/sk0fdFhRmE+E96fmN22hOLRJEAcPJK+5X1VTbRbP9qOt5aaaTwXHy07GHiELx0H1vcuhmM9wBVBpIa0GeceKyvs9Owd4VKQD1qaF902z4zPUc/TBorG86hsOl5UmZpXaOdkpwPeo9PYNl3blxc+3IEOmEK1KslRqWllPhulU1WkzPgp2fZbF/Oc89TlnVAoFlAS2oKOdpuYzPPlK/UDhREgoWlH2Y0pSzovZTIl0Gdkp4G/IGjaU3ffdcHxWazryNafAR6scVywV6mXvikPW2p+Fdl7Tqmxl7qn18dr43lcuP0kXh2+XZCjUEh5i4gMFXRV+RoJ5PqOJC1E4COj4vKVrp5gE7RaebLb2I9mHm2qreLYfGVluqk9O7lLN+x8ptOD6/IvbjP9peKLSQlpt5R0pKt3vaAkPFPAYrb1e5TG+4skNNiNHHyy+E6UGCgfLShurysS5U2oOA36SLN0e63W8tCpkCtGqJEulppX15FhOOSpOm/FRsOszLC6mPudM4auySgJb0LFO85VIO/XDNbdrRYpWlP2YlJSzYjZToqRMIdkdRRsM93nMUsqs0Zw+xH7t/T5OZfgW2wdML7smhQtEAc6CN/7e2rlcje7ft36SmObF+YmueAge3oUfIdnQRXvg7SEkMD8/XApkUO+Dfsze2RImF1Y0RUC8nPM0eXuf4GQt9fkJE2s/slspLNAYIPn+hlE824+Mj2JS/dGcqJhz4nf/OWEiCRWM2amWqs5COkCcZh8pavxq6GO0n87C9sG6rQrqy++rvCE9+mBRx672OlhW9mBUmTl3HwLxJMZn26/bFutFnW09yVKnaWU9HSwdHRWnzfgo9NRXtriY+hTK7j0rLUGPoCOdpj/Ex3T9DURZKVO2oujHtKScE7OZEmVlOslOFG0ou2/+evsUzm+bh11zl31l6mIbn8fVy057+hyULDPb66Zp7lrzzq6bp/srPtpZ+KmRDZWJjSsdUB1x2zR/d49N80u75KpJLWo5vXP1+enxU/0c3nrrNtxJxe31G3H+y5VobTb2a38WJeG881hyuXi6n7NLGU+KyaJnc0U3HpvLvLupR/rVkxVpf5Mdp8ZCioG64Borqgty09yqkDpTygIaHHmwaMIojsuJA2VlH+UqMxFWbP5lNCgX6eyWdshyqC9ZajR1VNXTxdLRUXHajI9CT31li7upz6/hlJ7EUhL0CdprRO60267tp5Y12b+LYUXhFHZMSsoZMZspUVamk+xM0YaS+9SqFuZIwY8h9Kvga6BpseG33sGPgAZZ8rgqOGbo+bNFpoHBkYJ+9YuhyaW6q0rwr/Pixlj6qgkcKTQ5jED+ZNCvfjF0jdJ/Xwv8EOgp2or74eC7Q09XL/E0MDha0K9+MXRPrfM9UvATcZermAX+F6CHttJnK8APA/3qV0MXrLhKAXS5ilngfwF6a8X4YAn4IaBf/Wro46x4dhDQnfbSs8Dg2KCRMiL5s0G/+uXQ52istwfAz+E0edMDHC1ugIRH/H84px/FN9HB/8f6rrkbeHMQAHAsXDcNnvAHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfggnJ/8BCHY8ItwMgI4AAAAASUVORK5CYII=)
"""

import pandas as pd
import numpy as np

dados = {'Aluno' : ["Ana", "Maria", "José", "Julia", "Claudio"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]}
ids = [10, 11, 12, 13, 14]
dfalunos = pd.DataFrame(data=dados, index=ids)
display(dfalunos)

dfalunos = pd.DataFrame({'Aluno' : ["Ana", "Maria", "José", "Julia", "Claudio"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})
dfalunos

"""# **PROPRIEDADES MAIS COMUNS**

**dataframe.dtypes**: verifica os tipos de dados que compõe as colunas
"""

dfalunos.dtypes

"""**dataframe.columns**: acessar a lista de colunas"""

dfalunos.columns

"""**dataframe['coluna']**: nomes das colunas podem ser usadas pra acessar seus valores

"""

dfalunos['Aluno']

"""
**dataframe.describe()**: verificar resumidamente a disposição estatística dos dados numéricos
"""

display(dfalunos)
dfalunos.describe()

"""
**dataframe.sort_values(by='coluna')**: ordená-los por determinada coluna
"""

dfalunos.sort_values('Prova', ascending=False)

"""
**dataframe.loc[indice]**: selecionar valor específico pelo índice
"""

dfalunos.loc[3]

"""
**dataframe[condição]**: selecionar de acordo com critérios condicionais
"""

dfalunos[dfalunos['Seminário'] > 8]

"""
**dataframe[(condição 1) operador (condição 2)**]: checar condições de múltiplas colunas.

**Operadores**: & (e), | (ou) e ! (não)"""

dfalunos[(dfalunos['Seminário'] > 8.0) & (dfalunos['Prova'] > 3)]

"""# **LEITURA E SELEÇÃO DE DADOS**

**dataframe = pd.read_csv('arquivo.csv')**: lendo um arquivo csv para um dataframe
"""

dfdados = pd.read_csv("dados.csv")
display(dfdados)

dfdados.shape # mostra a qtde de linhas e colunas

dfdados.T #mostra o dataframe como uma matriz transposta

"""**dataframe.head()**:  visualizar as primeiras linhas de um DataFrame

**daframe.tail()**:  visualizar as ultimas linhas de um DataFrame
"""

dfdados.head(10) #pode-se inserir a qtde de linhas q se deseja ver dfdados.head(10)

dfdados.tail(10) #pode-se inserir a qtde de linhas q se deseja ver dfdados.tail(10)

"""**dataframe['coluna'].unique()**: mostra a coluna desejada como valor unico"""

dfdados["bairro"].unique()

"""**dataframe['coluna'].value_counts()**: conta a qtde de elementos da coluna especificada"""

dfdados['bairro'].value_counts()

"""**dataframe['coluna'].value_counts(normalize=True)**: valores contados podem ser normalizados para expressar porcentagens"""

dfdados['bairro'].value_counts(normalize=True)

"""**dataframe.groupby('coluna').mean()**: agrupar o nosSo DataFrame pelos valores da coluna desejada, e em seguida aplicar o .mean() para se ter um objeto GroupBy com informação das médias agrupadas pelos valores da coluna desejada."""

dfdados.groupby('bairro').mean().round(2)

"""**dataframe.groupby('coluna').mean()['coluna a ser extraida'].sort_values()**: extrairmos dados de uma coluna obtendo o valor da média e classificado."""

dfdados.groupby('bairro').mean()['area'].sort_values()

"""**Aplicar uma função na seleção**"""

def truncar(bairro):
    return bairro[:3]

dfdados['bairro'].apply(truncar)

"""**O que são expressões Lambda no Python?**

As funções Lambda são chamadas de funções anônimas.

Nada mais são do que funções que o usuário não precisa definir, ou seja, não vai precisar escrever a função e depois utilizá-la dentro do código.
"""

dfdados["bairro"].apply(lambda x: x[:3])

"""## **Tratando dados Incompletos (NaN - Not a Number)**

**np.nan**: valor especial definido no Numpy, sigla para Not a Number
"""

df2 = dfdados.head() #cria um df temporário
df2

df2 = df2.replace({'pm2': {12031.25: np.nan}})
# troca um valor por np.nan

df2

"""**dropna()**: retorna as linhas que não contém um NaN"""

df2.dropna()

"""**dataframe.fillna(valor)**: preencher todos os valores NaN por um outro valor."""

df2.fillna(99)

"""**datafram.isna()**: indicar quais valores de um dataframe são NaN e quais não são"""

df2.isna()

df2

"""# **VISUALIZAÇÃO DE DADOS**

**.plot.hist()**: histograma
"""

# cria histograma com a coluna preco
# escala: *10^7
# padrão 10 bins: divide o dado em 10 partes
dfdados["preco"].plot.hist()

dfdados["preco"].plot.hist(bins=10, edgecolor='black')

""".**plot.bar()**: barras verticais
.**plot.bar()**: barras verticais horizontais
"""

dfdados["bairro"].value_counts().plot.bar()

dfdados["bairro"].value_counts().plot.barh(title="Número de Aptos")

"""**.plot.scatter(x, y, size, color)**: dispersão"""

import matplotlib.pyplot as plt

plt.style.use('ggplot')
dfdados.plot.scatter(x='pm2', y='area',s=5)
#s: tamanho dos pontos
#c: cor dos pontos

#O .sample pode receber tanto um argumento frac,
#que determina uma fração dos itens que o método retornará (no caso abaixo, 10%)
dfdados.sample(frac=0.1).plot.scatter(x='preco', y='area')

"""**.plot.pie()**: gráfico de pizza"""

dfdados["quartos"].value_counts().plot.pie()

"""**Extra: salvando seu dataframe**"""

df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})


df.to_csv("aulas.csv")
pd.read_csv("aulas.csv")