const form = document.querySelector('form')
const link = document.querySelector('a')

form.addEventListener('submit', function(e) {
	e.preventDefault()
	link.click()
})