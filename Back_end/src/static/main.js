const carsDataBox = document.getElementById('brand-data-box')
const carInput = document.getElementById('cars')

const modelsDataBox = document.getElementById('models-data-box')
const modelInput = document.getElementById('models')

$.ajax({
    type: 'GET',
    url: '/cars-json/',
    success: function(response){
        const carsData=response.data
        carsData.map(item=>{
            const option = document.createElement('option')
            option.textContent = item.name
            option.setAttribute('value', item.name)
            carsDataBox.appendChild(option)
        })
    },
    error: function(error){
        console.log(error)
    }
})

carInput.addEventListener('change', e=>{
    const selectedCar=e.target.value

    modelsDataBox.innerHTML=""

    $.ajax({
        type: 'GET',
        url: `models-json/${selectedCar}/`,
        success: function(response){
            console.log(response)
            const modelsData = response.data
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.name
                option.setAttribute('value', item.name)
                modelsDataBox.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})

