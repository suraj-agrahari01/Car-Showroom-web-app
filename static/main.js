

console.log("hello this is me")
const url=window.location.href

const searchForm=document.getElementById('search-form')
const searchinput=document.getElementById('search-input')
const result_box=document.getElementById('result-box')
const csrf_token=document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData =(customer) => {
 $.ajax({
     type:'POST',
     url: "http://127.0.0.1:8000/search_result/",
     data:{
         'csrfmiddlewaretoken':csrf_token,
         'customer':customer,

     },
     success:(res)=>{
         const uri="http://127.0.0.1:8000"
         console.log(res.data)
         const data=res.data
         if(Array.isArray(data)){
            result_box.innerHTML=""
            data.forEach(customer=>{
               
                result_box.innerHTML+=`
                <a href="${uri}/${customer.pk} " class="item">
                <div class="row mt-2 mb-2">
                <div class ="col-6">
                <h5> ${customer.name}</h5>
               
                </div>
                <div class ="col-6">
                <h5> ${customer.email}</h5>
                </div>
                </div>

                </a>

                `
               
            })
         }
         else{
             if(searchinput.value.length>0){
                 result_box.innerHTML=`<b> ${data}</b>`
             }
             else{
                 result_box.classList.add('not-visible')
             }
         }
     },
     error:(err)=>{
         console.log(err)
     }
 })
}

searchinput.addEventListener('keyup',e=>{
    console.log(e.target.value)

    if(result_box.classList.contains('not-visible')){
        result_box.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)
    
})
