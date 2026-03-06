import Card from '../card/card.component';
import './card-list.styles.css';

const CardList = ({ monsters }) => {
  return (
    <div className="card-list-container">
      {monsters.map(({ name, email, id }, index) => {
        return (
          <Card key={`${name}-${index}`} name={name} email={email} id={id} />
        );
      })}
    </div>
  );
};

export default CardList;
