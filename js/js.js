
document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    navLinks.forEach(link => {
        link.addEventListener("click", function () {

            navLinks.forEach(item => {
                item.classList.remove("active");
            });

            this.classList.add("active");
        });
    });
});



const testimonials = [

{
    image:"https://randomuser.me/api/portraits/women/44.jpg",
    name:"Priya Sharma",
    city:"Delhi",
    stars:"★★★★★",
    text:"Mummy Papa Home Care Services has been a blessing for our family. The caregivers are kind, professional and truly care for our loved ones."
},

{
    image:"https://randomuser.me/api/portraits/men/32.jpg",
    name:"Rohit Verma",
    city:"Noida",
    stars:"★★★★★",
    text:"Very professional service. The caregiver was trained, punctual and extremely supportive."
},

{
    image:"https://randomuser.me/api/portraits/women/68.jpg",
    name:"Anjali Gupta",
    city:"Gurugram",
    stars:"★★★★★",
    text:"Excellent experience. The staff treated my parents with dignity and genuine care."
}

];

let current = 0;

const text = document.querySelector(".testimonial-text");
const img = document.getElementById("clientImg");
const name = document.getElementById("clientName");
const city = document.getElementById("clientCity");
const stars = document.getElementById("clientStars");
const dots = document.querySelectorAll(".dot");

function showTestimonial(index){

    text.innerText = testimonials[index].text;
    img.src = testimonials[index].image;
    name.innerText = testimonials[index].name;
    city.innerText = testimonials[index].city;
    stars.innerText = testimonials[index].stars;

    dots.forEach(dot => dot.classList.remove("active"));
    dots[index].classList.add("active");
}

showTestimonial(0);

setInterval(() => {

    current++;

    if(current >= testimonials.length){
        current = 0;
    }

    showTestimonial(current);

},3000);



const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach(item => {

    const question = item.querySelector(".faq-question");

    question.addEventListener("click", () => {

        faqItems.forEach(faq => {

            if(faq !== item){
                faq.classList.remove("active");
            }

        });

        item.classList.toggle("active");

    });

});

