import Image from 'next/image'
import { Inter } from 'next/font/google'
import { data } from 'autoprefixer';

const inter = Inter({ subsets: ['latin'] })

export default function Home({ data, error }) {
  console.log('data: >> ', data);
  console.log('error: >> ', error);

  return (
    <>
      <p>Clothes</p>
      {data.map((element) =>
        <div key={element.slug}>
          <div>
            <Image src={"https://res.cloudinary.com/dt2nnnvpe/" + element.image} height={120} width={120} alt="Clothing Image" />
          </div>
          <div>
            <h1>{element.title}</h1>
            <p>{element.description}</p>
            <p>{element.created_at}</p>
          </div>
        </div>)}
    </>
  )
}

// fetches at build time
export async function getStaticProps() {
  let data = []
  let error = null

  try {
    const response = await fetch("http://localhost:8000/apiclothes")

    data = await response.json()

  } catch (err) {
    console.log('err :>> ', err)
    error = err
  }

  if (!data.length) {
    return {
      notFound: true
    }
  }

  return {
    props: {
      data: data,
      error: error,
    }
  }
}
