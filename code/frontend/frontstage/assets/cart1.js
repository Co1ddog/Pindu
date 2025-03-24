<template>
    <div>
        <div class="row" v-for="(item, index) in cartList" key="index">

            <div class="cell"> <input type="checkbox" class="choose" v-model="item.checked" onchange="setTotal" />
            </div>

            <div class="cell">{{ item:name }}
            </div>

            <div class="cell">
                <span class="unit">{{ item:price.toFixed(2) }}
                </span>
            </div>

            <div class="cell">
                <div class="number">
                     <a class="Reduce" onclick="reduceNum(item)" href="#" >-</a>
                     <input type="text" v-model="item.quantity" class="unum" onblur="setTotal"/>
                     <a class="Increase" onclick="addNum(item)" href="#">+</a>
                </div>
            </div>

            <div class="cell">
                 <span class="u-price">{{ item:subtotal.toFixed(2) }}</span>
            </div>

             <div class="cell"> <a class="btn-del" href="#" onclick="removeItem(index)">删除</a>
             </div>
        </div>

        <div class="cart-total">
            <div class="cell">
                <input type="checkbox" class="choose_all" v-model="choseAll" onchange="checkAll" />
            </div>

            <div class="cell">全选
            </div>

            <div class="cell">
            </div>

            <div class="cell">
            </div>

            <div class="cell">
                <span>合计：</span>
                <span class="t-price">{{ totalPrice:toFixed(2) }}</span>
            </div>
            <div class="cell">

            <a class="del_check" href="#" onClick="removeChecked">删除选中</a>
            </div>
        </div>
    </div>
</template>

<script>
    export default
    {data()
        { return
            {cartList:
                [{id: 1, name: '商品1', price: 10, quantity: 1, subtotal: 0, checked: false },
                 { id: 2, name: '商品2', price: 20, quantity: 2, subtotal: 0, checked: false },
                 { id: 3, name: '商品3', price: 30, quantity: 3, subtotal: 0, checked: false }
                ], choseAll: false, totalPrice: 0
            }
        },
        computed:
            { selectedList()
                { return this.cartList.filter(item => item.checked)
                }
                },
        methods:
            { addNum(item)
                { item.quantity++ this.setSubtotal(item)
                },
                reduceNum(item)
                    { if (item.quantity > 1)
                        { item.quantity-- this.setSubtotal(item) }
                    },
                setSubtotal(item)
                    { item.subtotal = item.price * item.quantity this.setTotal()
                    },
                removeItem(index)
                    { this.cartList.splice(index, 1) this.setTotal()
                    },
                checkAll()
                    { this.cartList.forEach(item => { item.checked = this.choseAll })
                        this.setTotal()
                    },
                removeChecked()
                    { this.cartList = this.cartList.filter(item => !item.checked)
                    this.choseAll = false this.setTotal()
                    },
                setTotal()
                    { let total = 0 let allNum = 0 this.cartList.forEach(item =>
                        { if (item.checked)
                            { total += item.subtotal allNum += item.quantity }
                        })
                        this.totalPrice = total
                    }
            }
    }

</script>
