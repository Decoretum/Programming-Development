let placeholder = document.getElementById('drop');
        let result = document.getElementById('cost')
        let num = '{{x}}';
        let cost = '{{Current.Cost}}';

        placeholder.addEventListener('change',()=>{
            console.log(num);
            console.log(cost);
        result.innerHTML = cost;

        })
