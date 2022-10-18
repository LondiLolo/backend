// create function
const navSlide = function(){
    //select burger div and nav div from the DOM
    const burger = document.querySelectorAll(".burger");
    const nav = document.querySelector(".nav-links");
    // console.log(burger)
    // console.log(nav)

    //select all the links
const navLinks = nav.querySelectorAll(".nav-links li")

// toggle navigation
burger.addEventListener('click', function(){
    nav.classList.toggle("nav-active");

    navLinks.forEach((link, index) => {
        // console.log(link, index);
        if(link.style.animation === true){

            link.style.animation = '';
        }
        else{
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.2}s`
        }
    });

    // burger Animation
    burger.classList.toggle("toggle")



})
}
navSlide()

// Product filter section start
const btns = document.querySelectorAll(".btn");
// console.log(btns)
const blogItems = document.querySelectorAll(".card-itms")
// console.log(blogItems)

for(let i = 0; i < btns.length; i++){
  btns[i].addEventListener('click',function(e){
      e.preventDefault()
      const filter = e.target.dataset.filter

    //   create foreach loop
    blogItems.forEach((blogItem) =>{
        if(filter === "all"){
            blogItem.style.display = "flex";

        }else{
            if(blogItem.classList.contains(filter)){
                blogItem.style.display = "flex";

            }else{
                blogItem.style.display = "none";
            }
        }
    })
  })
}
// product filter section end

// search filter start
const search = document.querySelector('#search');
search.addEventListener("keyup", (e) => {
    e.preventDefault()
    const searchValue = search.ariaValueMax.toLocaleLowerCase().trim();

    // Loop through blog category

    for (let i = 0; i < blogItems.length; i++) {
        console.log(blogItems[i])
        if(blogItems[i].classList.contains(searchValue)){
            blogItems[i].style.display = 'flex';
        } else if( searchValue === ""){
            blogItems[i].style.display = 'flex';
        } else{
            blogItems[i].style.display = 'none';
        }
    }
})
console.log(search)
// search filter end