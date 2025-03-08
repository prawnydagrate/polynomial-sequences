# Polynomial sequences
My aim with this project is to investigate polynomial sequences, and:
* find a relationship between the degree of the polynomial and the
  * number of terms required to find the common difference
  * the common difference and the leading coefficient
* find a general 𝑛<sup>th</sup> term expression for any polynomial sequence of degree 𝑑

Of course, a quick Google search could satisfy my curiosity, but what's the fun in that?

## Findings
In a polynomial sequence 𝑎₃𝑛³ + 𝑎₂𝑛² + 𝑎₁𝑛 + 𝑎₀:
<table>
	<tr>
		<th>𝑛</th>
		<td colspan="3">1</td>
		<td colspan="3">2</td>
		<td colspan="3">3</td>
		<td colspan="3">4</td>
	</tr>
	<tr>
		<th>𝑢</th>
		<td colspan="3">𝑎₃ + 𝑎₂ + 𝑎₁ + 𝑎₀</td>
		<td colspan="3">8𝑎₃ + 4𝑎₂ + 2𝑎₁ + 𝑎₀</td>
		<td colspan="3">27𝑎₃ + 9𝑎₂ + 3𝑎₁ + 𝑎₀</td>
		<td colspan="3">64𝑎₃ + 16𝑎₂ + 4𝑎₁ + 𝑎₀</td>
	</tr>
	<tr>
		<th>𝑑₁</th>
		<td colspan="4">7𝑎₃ + 3𝑎₂ + 𝑎₁</td>
		<td colspan="4">19𝑎₃ + 5𝑎₂ + 𝑎₁</td>
		<td colspan="4">37𝑎₃ + 7𝑎₂ + 𝑎₁</td>
	</tr>
	<tr>
		<th>𝑑₂</th>
		<td colspan="6">12𝑎₃ + 2𝑎₂</td>
		<td colspan="6">18𝑎₃ + 2𝑎₂</td>
	</tr>
	<tr>
		<th>𝑑₃</th>
		<td colspan="12">6𝑎₃</td>
	</tr>
</table>

The common 3<sup>rd</sup> difference shows that the sequence is cubic, and 𝑎₃ is found using the fact that the common 3<sup>rd</sup> difference is 6𝑎₃. The common difference (2<sup>nd</sup> and 1<sup>st</sup> respectively) in quadratic and linear sequences are 2𝑎₂ and 1𝑎₁. In any polynomial sequence of degree 𝑑, this project takes the coefficient of 𝑎<sub>𝑑</sub> in the common difference as 𝑞<sub>𝑑</sub>.

`qfind.py` shows that for any polynomial sequence of degree 𝑑, 𝑞<sub>𝑑</sub> = 𝑑!.
