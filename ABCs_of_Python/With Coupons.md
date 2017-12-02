# With Coupons

Update our function to take a list of price markups or markdowns. For example:

* we can now count **sales tax** as a markup (since it increases total due)
* we can count a coupon as a markdown (since it decreases total due)

You function will assume the first item in the list is tax markup. It should support at most 4 more coupon markdowns after that first item.

Remember, all coupons should be applied **before** taxes are applied. Additionally, if the markdowns render amount due to be less than 45% of the total before any price transformations, render all subsequent markdowns invalid.



